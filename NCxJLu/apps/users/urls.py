# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-19 下午 3:35'

from django.conf.urls import url,include

from .views import *

#{% url 'user':xxxxx %}

urlpatterns = [

    # 用户个人中心首页
    url(r'^info/$', UserInfoView.as_view(),name='info'),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(),name='image_upload'),

    # 用户修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(),name='update_pwd'),
]