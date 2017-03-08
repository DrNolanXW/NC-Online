# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-7 下午 4:04'

from django.conf.urls import url,include
from .views import *

#{% url 'course_list:xxxxx' %}

urlpatterns = [
    url(r'^$', CouserListView.as_view(), name='course'),

    url(r'^detail/(?P<demo_id>\d+)/$', CouserDetailView.as_view(), name='detail')

]