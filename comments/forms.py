# -*- conding:utf-8 -*-
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    # 表单内部类 Meta，指定一些和表单相关的东西
    class Meta:
        model = Comment # 表明这个表单的数据库模型是 Comment 类
        fields = ['name', 'email', 'url', 'text'] # 指定了表单需要显示的字段
