#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-01-11 23:42
# @Author  : mengjian
# @Site    : 
# @File    : forms.py
# @Software: PyCharm


from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']