# -*- conding:utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import Letter
from .forms import LetterForm
from django.conf import settings



def send(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            letter.save()
            msg = send_email(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['subject'], form.cleaned_data['message'])
            context = {'msg':msg}
            return render(request, 'blog/complete.html', context=context)
        else:
            context = {'form':form}
            return render(request, 'blog/contact.html', context=context)


def send_email(name, email, subject, message):
    from django.core.mail import EmailMultiAlternatives
    subject = subject
    text_content = '来自:' + '【饕餮鱼个人博客】' + '\n' + '姓名:' + name + '\n' + '对方邮箱:' + '<' + email + '>' + '\n' + '内容:' + message
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, ['heyifunobug@163.com'])
    msg.send()
    return '发送成功'