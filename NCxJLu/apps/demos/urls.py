# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-7 下午 4:04'

from django.conf.urls import url,include
from .views import *

#{% url 'course_list:xxxxx' %}

urlpatterns = [

    url(r'^$', CouserListView.as_view(), name='course'),

    url(r'^detail/(?P<demo_id>\d+)/$', CouserDetailView.as_view(), name='detail'),

    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),

    url(r'^info/(?P<demo_id>\d+)/$', CouserVideoView.as_view(), name='info'),

    url(r'^comment/(?P<demo_id>\d+)/$', CommentsView.as_view(), name='comment'),

    url(r'^add_comment/$',AddCommentView.as_view(),name='add_comment'),

    url(r'^video/(?P<video_id>\d+)/$',CouserVideoPlayView.as_view(),name='video_play'),

]