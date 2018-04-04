# -*- conding:utf-8 -*-
from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
    # 后去文章列表
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # 获取文章详情
    # [0-9]+ 表示匹配至少1为数字，(?P<pk>[0-9]+) 表示命名捕获组
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),

    # 后去归档
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesViwe.as_view(), name='archives'),

    # 获取分类
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),

    # 标签云
    url('^tag/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag'),

    # 搜索功能
    # url(r'^search/$', views.search, name='search'),

    url(r'^about/',views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^production/',views.production, name='production'),
]