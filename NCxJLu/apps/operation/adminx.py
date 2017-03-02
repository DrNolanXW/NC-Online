# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-2-8 下午 2:09'

import xadmin

from .models import UserAsk,CourseComments,UserFavorite,UserMessage,Usercourse

class UserAskAdmin(object):

    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentsAdmin(object):

    list_display = ['user', 'demo', 'comment', 'add_time']
    search_fields = ['user', 'demo', 'comment']
    list_filter = ['user', 'demo', 'comment', 'add_time']


class UserFavoriteAdmin(object):

    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user','fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):

    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):

    list_display = ['user', 'demo', 'add_time']
    search_fields = ['user', 'demo']
    list_filter = ['user', 'demo', 'add_time']

xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(Usercourse,UserCourseAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)

