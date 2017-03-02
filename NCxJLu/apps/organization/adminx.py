# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-2-8 下午 1:54'

import xadmin

from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):

    list_display = ['city', 'desc', 'add_time']
    search_fields = ['city', 'desc']
    list_filter = ['city', 'desc', 'add_time']


class CourseOrgAdmin(object):

    list_display = ['name', 'desc','fav_num','click_num','address' ,'city','add_time']
    search_fields = ['name', 'desc','fav_num','click_num','address' ,'city']
    list_filter = ['name', 'desc','fav_num','click_num','address','add_time']


class TeacherAdmin(object):

    list_display = ['org', 'name', 'work_years','work_company','work_position','point','add_time']
    search_fields = ['org', 'name', 'work_years','work_company','work_position','point']
    list_filter = ['org__name', 'name', 'work_years','work_company','work_position','point','add_time']

xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(CityDict,CityDictAdmin)