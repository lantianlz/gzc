# -*- coding: utf-8 -*-

import json
from django.db import transaction

from common import utils, cache, debug
from www.misc.decorators import cache_required
from www.misc import consts
from www.account.interface import UserBase
from www.message.models import UnreadCount, UnreadType, Notice, InviteAnswer, InviteAnswerIndex


dict_err = {
    40100: u'自己不能邀请自己哦',
    40101: u'最多邀请6人',
}
dict_err.update(consts.G_DICT_ERROR)

DEFAULT_DB = 'default'


class UnreadCountBase(object):

    """
    @note: 封装未读数信息操作类
    """

    def __init__(self):
        self.cache_obj = cache.Cache(config=cache.CACHE_TMP)

    def __del__(self):
        del self.cache_obj

    @cache_required(cache_key='unread_type_all', expire=0, cache_config=cache.CACHE_STATIC)
    def get_unread_type(self, must_update_cache=False):
        """
        @note: 获取提醒类型数据
        """
        return UnreadType.objects.all().order_by('type', 'id')

    def get_or_create_count_info(self, user):
        """
        @note: 获取用户未读数对象
        """
        user_id = utils.get_uid(user)
        obj_urcs = UnreadCount.objects.filter(user_id=user_id)
        created = True
        if not obj_urcs:
            count_info = self.init_count_info()
            urc = UnreadCount.objects.create(user_id=user_id, count_info=json.dumps(count_info))
            created = False
        else:
            urc = obj_urcs[0]
        return urc, created

    def init_count_info(self):
        """
        @note: 获取初始未读数信息
        """

        nts = self.get_unread_type()
        count_info = {}
        for nt in nts:
            count_info.setdefault(str(nt.code), 0)
        return count_info

    def update_unread_count(self, user, code, operate="add"):
        """
        @note: 更新提醒未读数
        """

        if UnreadType.objects.filter(code=code).count() == 0:
            return False

        urc, created = self.get_or_create_count_info(user)
        count_info = json.loads(urc.count_info)

        if not count_info.has_key(code):
            count_info.setdefault(code, 0)
        # 加一或者重置
        if operate == 'add':
            count_info[code] += 1
        else:
            count_info[code] = 0

        urc.count_info = json.dumps(count_info)
        urc.save()
        # 操作缓存
        user_id = utils.get_uid(user)
        cache_key = u'%s_%s' % ('unread_count', user_id)
        self.cache_obj.set(cache_key, count_info, 3600 * 24)

        return True

    @cache_required(cache_key='unread_count_%s', expire=3600 * 24)
    def get_unread_count_info(self, user):
        """
        @note: 获取未读数
        """
        user_id = utils.get_uid(user)
        try:
            count_info = json.loads(UnreadCount.objects.get(user_id=user_id).count_info)
        except UnreadCount.DoesNotExist:
            count_info = self.init_count_info()  # 没有就不用自动创建，更新的时候进行创建
        return count_info

    def get_unread_count_total(self, user):
        count_info = self.get_unread_count_info(user)
        return count_info

    def clear_count_info_by_code(self, user_id, code):
        """
        @note: 通用的清除消息数的方法，数字大于0的才去调用清除，提高效率
        """
        if code and user_id and int(UnreadCountBase().get_unread_count_info(user_id).get(code, 0)) > 0:
            UnreadCountBase().update_unread_count(user_id, code, operate='clear')

    def get_system_message(self, user_id):
        return Notice.objects.filter(user_id=user_id)

    def add_system_message(self, user_id, content, source=0):
        notice = Notice.objects.create(user_id=user_id, content=content, source=source)
        UnreadCountBase().update_unread_count(user_id, code='system_message')
        return notice


class InviteAnswerBase(object):

    def __init__(self):
        pass

    def format_invite_user(self, show_invite_users, invited_users):
        from www.custom_tags.templatetags.custom_filters import str_display

        show_invite_users_json = []
        invited_users_json = []
        invited_user_ids = [iu.to_user_id for iu in invited_users]

        for siu in show_invite_users:
            user = UserBase().get_user_by_id(siu.user_id)
            show_invite_users_json.append(dict(user_id=user.id, user_nick=user.nick, user_avatar=user.get_avatar_65(),
                                               user_des=str_display(user.des or '', 17), is_invited=siu.user_id in invited_user_ids))
        for iu in invited_users:
            invited_users_json.append(dict(user_id=iu.to_user_id, user_nick=UserBase().get_user_by_id(iu.to_user_id).nick))
        return show_invite_users_json, invited_users_json

    @transaction.commit_manually(using=DEFAULT_DB)
    def create_invite(self, from_user_id, to_user_id, question_id):
        try:
            from www.question.interface import QuestionBase

            ub = UserBase()
            try:
                assert ub.get_user_by_id(from_user_id) and ub.get_user_by_id(to_user_id) and QuestionBase().get_question_by_id(question_id)
            except:
                transaction.rollback(using=DEFAULT_DB)
                return 99800, dict_err.get(99800)

            if from_user_id == to_user_id:
                transaction.rollback(using=DEFAULT_DB)
                return 40100, dict_err.get(40100)

            # 同一个问题最多邀请6个人
            if InviteAnswerIndex.objects.filter(from_user_id=from_user_id, question_id=question_id).count() >= 6:
                transaction.rollback(using=DEFAULT_DB)
                return 40101, dict_err.get(40101)

            has_indexed = False
            need_update_unread_count = True
            try:
                ia = InviteAnswer.objects.create(from_user_ids=json.dumps([from_user_id, ]), to_user_id=to_user_id, question_id=question_id)
            except:
                ia = InviteAnswer.objects.get(to_user_id=to_user_id, question_id=question_id)
                from_user_ids = json.loads(ia.from_user_ids)
                print from_user_ids
                if from_user_id not in from_user_ids:
                    from_user_ids.append(from_user_id)
                else:
                    has_indexed = True
                ia.from_user_ids = json.dumps(from_user_ids)
                ia.save()

                need_update_unread_count = True if (ia.is_read and not has_indexed) else False

            # 建立索引
            if not has_indexed:
                InviteAnswerIndex.objects.create(from_user_id=from_user_id, to_user_id=to_user_id, question_id=question_id)

            # 更新未读消息，新邀请或者邀请已读才更新未读数
            if need_update_unread_count:
                UnreadCountBase().update_unread_count(to_user_id, code='invite_answer')

            transaction.commit(using=DEFAULT_DB)
            return 0, dict_err.get(0)
        except Exception, e:
            debug.get_debug_detail(e)
            transaction.rollback(using=DEFAULT_DB)
            return 99900, dict_err.get(99900)

    def get_user_received_invite(self, to_user_id):
        pass

    def get_invited_user_by_question_id(self, from_user_id, question_id):
        return InviteAnswerIndex.objects.filter(from_user_id=from_user_id, question_id=question_id)

    def update_invite_is_read(self, to_user_id):
        return InviteAnswer.objects.filter(to_user_id=to_user_id).update(is_read=True)
