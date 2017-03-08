# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-7 下午 4:04'
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import *


class CouserListView(View):

    def get(self,request):

        all_demo = Demo.objects.all().order_by('-add_time')
        hot_demo = Demo.objects.all().order_by('-click_num')[:3]

        #按热门与参与人数排名
        sort = request.GET.get('sort','')
        if sort == 'students':
            all_demo = all_demo.order_by('-students')
        elif sort == 'hot':
            all_demo = all_demo.order_by('-click_num')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_demo, 9, request=request)
        page_demo = p.page(page)

        return render(request,'course-list.html',{
            'all_demo': page_demo,
            'sort':sort,
            'hot_demo':hot_demo,
            'nav': 'course',
        })


class CouserDetailView(View):

    def get(self, request,demo_id):
        demo = Demo.objects.get(id = int(demo_id))

        #增加课程点击数
        demo.click_num += 1
        demo.save()

        return render(request,'course-detail.html',{
            'demo':demo,
        })