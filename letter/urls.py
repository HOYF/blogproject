# -*- conding:utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'letter'
urlpatterns = [
    url(r'^send/', views.send, name='send'),
]