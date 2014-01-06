# -*- coding: utf-8 -*-

import urllib
from pprint import pprint
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from common import utils, page
from www.question import interface
from www.misc.decorators import member_required


#@member_required
def question_home(request, question_type=0, template_name='question/question_home.html'):
    qb = interface.QuestionBase()
    questions = qb.get_questions(question_type_domain=question_type)

    # 分页
    page_num = int(request.REQUEST.get('page', 1))
    page_objs = page.Cpt(questions, count=1, page=page_num).info
    questions = page_objs[0]
    page_params = (page_objs[1], page_objs[4])

    questions = qb.format_quesitons(questions)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


#@member_required
def question_detail(request, question_id, template_name='question/question_detail.html'):
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


@member_required
def ask_question(request, template_name='question/ask_question.html'):
    if request.POST:
        question_type = int(request.POST.get('question_type', '0'))
        question_title = request.POST.get('question_title')
        question_content = request.POST.get('question_content')

        qb = interface.QuestionBase()
        flag, result = qb.create_question(request.user.id, question_type, question_title,
                                          question_content, ip=utils.get_clientip(request))
        if flag:
            return HttpResponseRedirect('/question/question_detail/%s' % result.id)
        else:
            error_msg = result
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
