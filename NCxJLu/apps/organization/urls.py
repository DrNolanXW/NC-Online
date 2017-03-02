# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-1 下午 6:17'
from django.conf.urls import url,include
from .views import OrgListView,AddUserAsk

urlpatterns = [
    # 课程机构首页
    url(r'^$', OrgListView.as_view(),name='org'),
    url(r'^add_ask/$', AddUserAsk.as_view(),name='add_ask')

]