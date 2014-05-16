# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from www.misc.decorators import staff_required, common_ajax_response
from www.misc import qiniu_client
from common import utils, page

from www.question.interface import QuestionBase


@staff_required
def important_question(request, template_name='admin/important_question.html'):
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


@staff_required
def get_important_question_by_title(request):
    title = request.POST.get('title')
    page_index = int(request.POST.get('page_index', 1))

    important_questions = QuestionBase().get_important_question_by_title(title)
    page_objs = page.Cpt(important_questions, count=10, page=page_index).info
    print page_objs
    data = []
    num = 0

    for important_question in page_objs[0]:
        num += 1
        data.append({
            'num': num,
            'question_id': important_question.question.id,
            'user_id': important_question.question.user.id,
            'user_nick': important_question.question.user.nick,
            'title': important_question.question.title,
            'description': important_question.question.content,
            'img': important_question.img,
            'img_alt': important_question.img_alt,
            'sort_num': important_question.sort_num,
            'create_time': str(important_question.question.create_time),
            'set_important_time': str(important_question.create_time)
        })

    return HttpResponse(
        json.dumps({'data': data, 'page_count': page_objs[4], 'total_count': page_objs[5]}),
        mimetype='application/json'
    )


@staff_required
def add_important(request):
    '''
    添加精选
    '''
    img = request.FILES.get('importantImg')
    flag, img_name = qiniu_client.upload_img(img, img_type='important')

    qb = QuestionBase()
    question_id = request.REQUEST.get('questionId')
    question = qb.get_question_by_id(question_id)

    img_alt = request.REQUEST.get('imgAlt', '')
    sort_num = request.REQUEST.get('sort', 0)

    code, msg = qb.set_important(question, request.user, img_name, img_alt, sort_num)

    url = ''
    if code == 0:
        iq = qb.get_important_question_by_question_id(question_id)
        url = '/admin/important_question#modify/%s' % iq.question.id
    else:
        url = request.META['HTTP_REFERER']
    return HttpResponseRedirect(url)


@staff_required
def modify_important(request):
    '''
    修改精选
    '''
    qb = QuestionBase()
    img_alt = request.REQUEST.get('imgAlt', '')
    sort_num = request.REQUEST.get('sort', 0)
    question_id = request.REQUEST.get('questionId')
    question = qb.get_question_by_id(question_id)

    img = request.FILES.get('importantImg')

    iq = qb.get_important_question_by_question_id(question_id)
    img_name = iq.img
    # 如果有上传图片
    if img:
        flag, img_name = qiniu_client.upload_img(img, img_type='important')

    code, msg = qb.set_important(question, request.user, img_name, img_alt, sort_num)

    url = '/admin/important_question#modify/%s' % iq.question.id

    return HttpResponseRedirect(url)


@staff_required
def get_important_question_by_question_id(request):
    question_id = request.REQUEST.get('question_id')

    data = ''
    important_question = QuestionBase().get_important_question_by_question_id(question_id)
    if important_question:
        data = {
            'question_id': important_question.question.id,
            'user_id': important_question.question.user.id,
            'user_nick': important_question.question.user.nick,
            'title': important_question.question.title,
            'description': important_question.question.content,
            'img': important_question.img,
            'img_alt': important_question.img_alt,
            'sort_num': important_question.sort_num,
            'create_time': str(important_question.question.create_time),
            'set_important_time': str(important_question.create_time)
        }

    return HttpResponse(json.dumps(data), mimetype='application/json')


@staff_required
@common_ajax_response
def cancel_important(request):
    question_id = request.REQUEST.get('question_id')

    qb = QuestionBase()
    question = qb.get_question_by_id(question_id)
    return qb.cancel_important(question, request.user)
