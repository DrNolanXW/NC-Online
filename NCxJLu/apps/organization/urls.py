# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-1 下午 6:17'

from django.conf.urls import url,include

from .views import OrgListView,AddUserAskView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeacherView
from .views import AddOrgFavView

#{% url 'org_list':xxxxx %}

urlpatterns = [

    # 课程机构首页
    url(r'^$', OrgListView.as_view(),name='org'),

    url(r'^add_ask/$', AddUserAskView.as_view(),name='add_ask'),

    #  d+ 正则表达式取纯数字
    url(r'^home/(?P<org_id>\d+)/$',OrgHomeView.as_view(),name='org_home'),

    url(r'^course/(?P<org_id>\d+)/$',OrgCourseView.as_view(),name='org_course'),

    url(r'^desc/(?P<org_id>\d+)/$',OrgDescView.as_view(),name='org_desc'),

    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),

    # 机构收藏
    url(r'^add_org_fav/$', AddOrgFavView.as_view(), name='add_org_fav'),

]