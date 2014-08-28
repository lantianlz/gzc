# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

from common import page
from www.toutiao import interface

ab = interface.ArticleBase()
atb = interface.ArticleTypeBase()


def toutiao_list(request, article_type=None, template_name='toutiao/toutiao_list.html'):
    if not article_type:
        articles = ab.get_all_articles()
    else:
        article_type = atb.get_type_by_domain(article_type)
        if not article_type:
            raise Http404
        articles = ab.get_articles_by_type(article_type)

    # 分页
    page_num = int(request.REQUEST.get('page', 1))
    page_objs = page.Cpt(articles, count=10, page=page_num).info
    articles = page_objs[0]
    page_params = (page_objs[1], page_objs[4])

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def toutiao_detail(request, article_id, template_name='toutiao/toutiao_detail.html'):
    article = ab.get_article_by_id(article_id)
    if not article:
        raise Http404
    article = ab.format_articles([article, ])[0]
    newsest_articles = ab.get_newsest_articles_by_weixin_mp(article)[:5]
    ab.add_article_view_count(article_id)

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
