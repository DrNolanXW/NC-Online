# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import CourseOrg,CityDict
from .forms import UserAskForm

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class OrgListView(View):

    #课程机构列表功能
    def get(self,request):

        all_orgs = CourseOrg.objects.all()
        all_citys = CityDict.objects.all()

        hot_orgs = all_orgs.order_by('click_num')[:3]

        # 筛选城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        #类别筛选
        categroy = request.GET.get('ct','')
        if categroy:
            all_orgs = all_orgs.filter(categroy=categroy)

        #学习人数排名
        sort = request.GET.get('sort','')
        if sort == 'students':
            all_orgs = all_orgs.order_by('-students')
        elif sort == 'courses':
            all_orgs = all_orgs.order_by('-couser_num')

        # 对教程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs,5, request=request)
        page_orgs = p.page(page)


        org_nums = all_orgs.count()
        return render(request,'org-list.html',{
            'all_orgs':page_orgs,
            'all_citys':all_citys,
            'org_nums':org_nums,
            'city_id':city_id,
            'categroy':categroy,
            'hot_orgs':hot_orgs,
            'sort':sort
        })


class AddUserAsk(View):

    # 用户添加咨询
    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            # 异步操作
            user_ask = userask_form.save(commit=True)
            return HttpResponse("{'status':'success'}", content_type='application/json')
        else:
            # return HttpResponse("{'status':'fail','msg':{0}}".format(userask_form.errors),
            #                     content_type='application/json')
            return  HttpResponse("{'status':'fail','msg':'提交出错'}", content_type='application/json')