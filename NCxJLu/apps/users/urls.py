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

    # 我的课程
    url(r'^my/couser/$', MyCouserView.as_view(), name='my_couser'),

    # 我的收藏机构
    url(r'^my/fav/org/$', MyFavOrgView.as_view(), name='my_fav_org'),

    # 我的收藏课程
    url(r'^my/fav/course/$', MyFavCourseView.as_view(), name='my_fav_course'),

    # 我的收藏教师
    url(r'^my/fav/teacher/$', MyFavTeacherView.as_view(), name='my_fav_teacher'),

    # 我的消息
    url(r'^my/message/$', MyMessageView.as_view(), name='my_message'),
]