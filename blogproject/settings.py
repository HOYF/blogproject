# -*- conding:utf-8 -*-
"""
Django settings for blogproject project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e&7im!#&2)1^s45zo4vssl#aj89&zxof*2a1@1udltcc+k$oc$'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# 发布生产需要更改为 False
DEBUG = False

# ALLOWED_HOSTS = []
# 发布生产需要更改为
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.sohoho.xin']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'blog',
    'comments',
    'letter',
]

HAYSTACK_CONNECTIONS = {
    'default':{
        'ENGINE':'blog.whoosh_cn_backend.WhooshEngine', # 指定了 django haystack 使用的搜索引擎，这里我们使用了 blog.whoosh_cn_backend.WHooshEngine ，虽然目前这个引擎还不存在，但我们接下来会创建它
        'PATH':os.path.join(BASE_DIR,'whoosh_index'), # 制定了索引文件需要存放的位置，我们设置了为项目根目录 BASE_DIR 下的 whoosh_index 文件夹
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10 # 指定如何对搜索结果分页，这里我们设置为每10项结果为一页
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor' # 这个作用是每当有文章更新时就更新索引，由于博客文章更新不会太频繁，因此实时更新没有问题

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans' #把英文改为中文

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai' #把国际时区改为中国时区

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# 发布生产添加这行代码，指明静态文件的手机目录
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 邮件发送配置
# 指定发送邮件的后端模块，大多数情况下照抄
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# 发送方的smtp服务器地址
EMAIL_HOST = 'smtp.163.com'
# smtp服务端口，默认为25
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = 'heyifunobug@163.com'
# 在邮箱中设置的客户端授权码
EMAIL_HOST_PASSWORD = 'wing449120275HO'
# 收件人看到的发件人
EMALL_FROM = '来自个人博客<heyifunobug@163.com>'
# 注册有效期天数
# CONFIRM_DAYS = 7