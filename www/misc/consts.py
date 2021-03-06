# -*- coding: utf-8 -*-

'''
全局常量维护
'''

G_DICT_ERROR = {
    99600: u'不存在的用户',
    99700: u'权限不足',
    99800: u'参数缺失',
    99900: u'系统错误',
    0: u'成功'
}


PERMISSIONS = [
    #{'code': 'is_administrator', 'name': u'能否进入管理后台', 'parent': None},
    {'code': 'permission_manage', 'name': u'权限管理', 'parent': None},
    {'code': 'add_user_permission', 'name': u'添加用户权限', 'parent': 'permission_manage'},
    {'code': 'query_user_permission', 'name': u'查询用户权限', 'parent': 'permission_manage'},
    {'code': 'modify_user_permission', 'name': u'修改用户权限', 'parent': 'permission_manage'},
    {'code': 'cancel_admin', 'name': u'取消管理员', 'parent': 'permission_manage'},

    {'code': 'manage_recommend_user', 'name': u'推荐用户管理', 'parent': None},
    {'code': 'set_recommend_user', 'name': u'设置推荐用户', 'parent': 'manage_recommend_user'},
    {'code': 'query_recommend_user', 'name': u'查询推荐用户信息', 'parent': 'manage_recommend_user'},
    {'code': 'modify_recommend_user', 'name': u'修改推荐用户顺序', 'parent': 'manage_recommend_user'},
    {'code': 'cancel_recommend_user', 'name': u'取消推荐用户', 'parent': 'manage_recommend_user'},

    {'code': 'important_question_manage', 'name': u'每日精选管理', 'parent': None},
    {'code': 'add_important_question', 'name': u'添加每日精选', 'parent': 'important_question_manage'},
    {'code': 'query_important_question', 'name': u'查询每日精选', 'parent': 'important_question_manage'},
    {'code': 'modify_important_question', 'name': u'修改每日精选', 'parent': 'important_question_manage'},
    {'code': 'cancel_important_question', 'name': u'取消每日精选', 'parent': 'important_question_manage'},

    {'code': 'question_manage', 'name': u'提问管理', 'parent': None},
    #{'code': 'add_question', 'name': u'添加提问', 'parent': 'question_manage'},
    {'code': 'query_question', 'name': u'查询提问', 'parent': 'question_manage'},
    {'code': 'modify_question', 'name': u'修改提问', 'parent': 'question_manage'},
    {'code': 'remove_question', 'name': u'删除提问', 'parent': 'question_manage'},

    {'code': 'user_manage', 'name': u'用户管理', 'parent': None},
    #{'code': 'add_user', 'name': u'添加用户', 'parent': 'user_manage'},
    {'code': 'query_user', 'name': u'查询用户', 'parent': 'user_manage'},
    {'code': 'modify_user', 'name': u'修改用户', 'parent': 'user_manage'},
    {'code': 'remove_user', 'name': u'删除用户', 'parent': 'user_manage'},

    {'code': 'customer_manager_manage', 'name': u'客户经理管理', 'parent': None},
    {'code': 'add_customer_manager', 'name': u'添加客户经理', 'parent': 'customer_manager_manage'},
    {'code': 'query_customer_manager', 'name': u'查询客户经理', 'parent': 'customer_manager_manage'},
    {'code': 'modify_customer_manager', 'name': u'修改客户经理', 'parent': 'customer_manager_manage'},
    {'code': 'remove_customer_manager', 'name': u'删除客户经理', 'parent': 'customer_manager_manage'},

    {'code': 'friendly_link_manage', 'name': u'友情链接管理', 'parent': None},
    {'code': 'add_friendly_link', 'name': u'添加友情链接', 'parent': 'friendly_link_manage'},
    {'code': 'query_friendly_link', 'name': u'查询友情链接', 'parent': 'friendly_link_manage'},
    {'code': 'modify_friendly_link', 'name': u'修改友情链接', 'parent': 'friendly_link_manage'},
    {'code': 'remove_friendly_link', 'name': u'删除友情链接', 'parent': 'friendly_link_manage'},

    {'code': 'statistics_manage', 'name': u'统计管理', 'parent': None},
    {'code': 'statistics_active_user', 'name': u'当日活跃用户统计', 'parent': 'statistics_manage'},
    {'code': 'statistics_register_user', 'name': u'注册用户统计', 'parent': 'statistics_manage'},
    {'code': 'statistics_questions', 'name': u'提问统计', 'parent': 'statistics_manage'},
    {'code': 'statistics_answers', 'name': u'回答统计', 'parent': 'statistics_manage'},
    {'code': 'statistics_spider_access', 'name': u'蜘蛛访问统计', 'parent': 'statistics_manage'},

    {'code': 'tools', 'name': u'常用工具', 'parent': None},
    {'code': 'get_cache', 'name': u'查询缓存', 'parent': 'tools'},
    {'code': 'remove_cache', 'name': u'删除缓存', 'parent': 'tools'},
    {'code': 'modify_cache', 'name': u'修改缓存', 'parent': 'tools'},
    {'code': 'query_notice', 'name': u'查询全站通告', 'parent': 'tools'},
    {'code': 'add_notice', 'name': u'添加全站通告', 'parent': 'tools'},
    {'code': 'modify_notice', 'name': u'修改全站通告', 'parent': 'tools'},
    {'code': 'remove_notice', 'name': u'删除全站通告', 'parent': 'tools'},

    {'code': 'topic_manage', 'name': u'话题管理', 'parent': None},
    {'code': 'add_topic', 'name': u'添加话题', 'parent': 'topic_manage'},
    {'code': 'query_topic', 'name': u'查询话题', 'parent': 'topic_manage'},
    {'code': 'modify_topic', 'name': u'修改话题', 'parent': 'topic_manage'},
    #{'code': 'remove_topic', 'name': u'查询全站通告', 'parent': 'topic_manage'},

    {'code': 'city_manage', 'name': u'城市管理', 'parent': None},
    #{'code': 'add_city', 'name': u'添加城市', 'parent': 'city_manage'},
    {'code': 'query_city', 'name': u'查询城市', 'parent': 'city_manage'},
    {'code': 'modify_city', 'name': u'修改城市', 'parent': 'city_manage'},
    #{'code': 'remove_city', 'name': u'删除营业部', 'parent': 'city_manage'},

    {'code': 'district_manage', 'name': u'区管理', 'parent': None},
    #{'code': 'add_district', 'name': u'添加区', 'parent': 'district_manage'},
    {'code': 'query_district', 'name': u'查询区', 'parent': 'district_manage'},
    {'code': 'modify_district', 'name': u'修改区', 'parent': 'district_manage'},
    #{'code': 'remove_district', 'name': u'删除区', 'parent': 'district_manage'},

    {'code': 'department_manage', 'name': u'营业部管理', 'parent': None},
    {'code': 'add_department', 'name': u'添加营业部', 'parent': 'department_manage'},
    {'code': 'query_department', 'name': u'查询营业部', 'parent': 'department_manage'},
    {'code': 'modify_department', 'name': u'修改营业部', 'parent': 'department_manage'},
    #{'code': 'remove_department', 'name': u'删除营业部', 'parent': 'department_manage'},

    {'code': 'zhuanti_manage', 'name': u'专题管理', 'parent': None},
    {'code': 'add_zhuanti', 'name': u'添加专题', 'parent': 'zhuanti_manage'},
    {'code': 'query_zhuanti', 'name': u'查询专题', 'parent': 'zhuanti_manage'},
    {'code': 'modify_zhuanti', 'name': u'修改专题', 'parent': 'zhuanti_manage'},
    {'code': 'remove_zhuanti', 'name': u'删除专题', 'parent': 'zhuanti_manage'},

    {'code': 'article_manage', 'name': u'资讯管理', 'parent': None},
    {'code': 'add_article', 'name': u'添加资讯', 'parent': 'article_manage'},
    {'code': 'query_article', 'name': u'查询资讯', 'parent': 'article_manage'},
    {'code': 'modify_article', 'name': u'修改资讯', 'parent': 'article_manage'},
    {'code': 'remove_article', 'name': u'删除资讯', 'parent': 'article_manage'},

    {'code': 'stock_manage', 'name': u'个股管理', 'parent': None},
    {'code': 'add_stock', 'name': u'添加个股', 'parent': 'stock_manage'},
    {'code': 'query_stock', 'name': u'查询个股', 'parent': 'stock_manage'},
    {'code': 'modify_stock', 'name': u'修改个股', 'parent': 'stock_manage'},
    {'code': 'remove_stock', 'name': u'删除个股', 'parent': 'stock_manage'},

    {'code': 'stock_feed_manage', 'name': u'股票动态管理', 'parent': None},
    {'code': 'add_stock_feed', 'name': u'添加股票动态', 'parent': 'stock_feed_manage'},
    {'code': 'query_stock_feed', 'name': u'查询股票动态', 'parent': 'stock_feed_manage'},
    {'code': 'modify_stock_feed', 'name': u'修改股票动态', 'parent': 'stock_feed_manage'},
    {'code': 'remove_stock_feed', 'name': u'删除股票动态', 'parent': 'stock_feed_manage'},

    {'code': 'toutiao_type_manage', 'name': u'头条类型管理', 'parent': None},
    {'code': 'add_toutiao_type', 'name': u'添加头条类型', 'parent': 'toutiao_type_manage'},
    {'code': 'query_toutiao_type', 'name': u'查询头条类型', 'parent': 'toutiao_type_manage'},
    {'code': 'modify_toutiao_type', 'name': u'修改头条类型', 'parent': 'toutiao_type_manage'},
    # {'code': 'remove_toutiao_type', 'name': u'删除头条类型', 'parent': 'toutiao_type_manage'},

    {'code': 'weixin_mp_manage', 'name': u'微信号管理', 'parent': None},
    {'code': 'add_weixin_mp', 'name': u'添加微信号', 'parent': 'weixin_mp_manage'},
    {'code': 'query_weixin_mp', 'name': u'查询微信号', 'parent': 'weixin_mp_manage'},
    {'code': 'modify_weixin_mp', 'name': u'修改微信号', 'parent': 'weixin_mp_manage'},
    # {'code': 'remove_weixin_mp', 'name': u'删除微信号', 'parent': 'weixin_mp_manage'},

    {'code': 'toutiao_article_manage', 'name': u'头条文章管理', 'parent': None},
    {'code': 'add_toutiao_article', 'name': u'添加头条文章', 'parent': 'toutiao_article_manage'},
    {'code': 'query_toutiao_article', 'name': u'查询头条文章', 'parent': 'toutiao_article_manage'},
    {'code': 'modify_toutiao_article', 'name': u'修改头条文章', 'parent': 'toutiao_article_manage'},
    # {'code': 'remove_toutiao_article', 'name': u'删除微信号', 'parent': 'toutiao_article_manage'},

    {'code': 'toutiao_bankey_manage', 'name': u'头条关键字管理', 'parent': None},
    {'code': 'add_toutiao_bankey', 'name': u'添加关键字', 'parent': 'toutiao_bankey_manage'},
    {'code': 'query_toutiao_bankey', 'name': u'查询关键字', 'parent': 'toutiao_bankey_manage'},
    {'code': 'remove_toutiao_bankey', 'name': u'修改关键字', 'parent': 'toutiao_bankey_manage'},

    {'code': 'external_cm_manage', 'name': u'外部客户经理管理', 'parent': None},
    #{'code': 'add_customer_manager', 'name': u'添加客户经理', 'parent': 'external_cm_manage'},
    {'code': 'query_external_cm', 'name': u'查询外部客户经理', 'parent': 'external_cm_manage'},
    {'code': 'modify_external_cm', 'name': u'修改外部客户经理', 'parent': 'external_cm_manage'},
    #{'code': 'remove_customer_manager', 'name': u'删除客户经理', 'parent': 'external_cm_manage'},
    
    {'code': 'invitation_manage', 'name': u'邀请注册管理', 'parent': None},
    {'code': 'query_invitation', 'name': u'查询邀请注册信息', 'parent': 'invitation_manage'},

    {'code': 'stock_chart_manage', 'name': u'股票图表管理', 'parent': None},
    {'code': 'query_stock_chart', 'name': u'查询股票图表', 'parent': 'stock_chart_manage'},

    {'code': 'kind_manage', 'name': u'股票行业管理', 'parent': None},
    {'code': 'add_kind', 'name': u'添加行业', 'parent': 'kind_manage'},
    {'code': 'query_kind', 'name': u'查询行业', 'parent': 'kind_manage'},
    {'code': 'modify_kind', 'name': u'修改行业', 'parent': 'kind_manage'},
    {'code': 'remove_kind', 'name': u'删除行业', 'parent': 'kind_manage'},
]
