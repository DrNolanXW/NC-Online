# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-2-8 上午 1:59'
import xadmin

from .models import Demo,Lesson,Video,DemoResource


class DemoAdmin(object):

    list_display = ['name', 'desc', 'detail', 'degree','learn_time','students']
    search_fields = ['name', 'desc', 'detail', 'degree','students']
    list_filter = ['name', 'desc', 'detail', 'degree','learn_time','students']


class LessonAdmin(object):

    list_display = ['demo', 'name', 'add_time']
    search_fields = ['demo', 'name']
    list_filter = ['demo__name', 'name', 'add_time']


class VideoAdmin(object):

    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class DemoResourceAdmin(object):

    list_display = ['demo', 'name', 'downlaod', 'add_time']
    search_fields = ['demo', 'name', 'downlaod']
    list_filter = ['demo__name', 'name', 'downlaod', 'add_time']


xadmin.site.register(Demo,DemoAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(DemoResource,DemoResourceAdmin)