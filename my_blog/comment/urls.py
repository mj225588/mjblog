#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-01-11 23:51
# @Author  : mengjian
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]