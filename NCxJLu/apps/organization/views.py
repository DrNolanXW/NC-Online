# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.http import JsonResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg,CityDict,Teacher
from .forms import UserAskForm
from demos.models import Demo
from operation.models import UserFavorite


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
        p = Paginator(all_orgs,3, request=request)
        page_orgs = p.page(page)


        org_nums = all_orgs.count()
        return render(request,'org-list.html',{
            'all_orgs': page_orgs,
            'all_citys': all_citys,
            'org_nums': org_nums,
            'city_id': city_id,
            'categroy': categroy,
            'hot_orgs': hot_orgs,
            'sort': sort,
            'nav': 'org',
        })


class AddUserAskView(View):

    # 用户添加咨询
    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():

            # 异步操作
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            # return HttpResponse("{'status':'fail','msg':{0}}".format(userask_form.errors),
            #                     content_type='application/json')
            return HttpResponse('{"status":"fail","msg":"提交出错"}', content_type='application/json')


class OrgHomeView(View):

    #机构首页
   def get(self,request,org_id):

       current_page = 'home'
       course_org = CourseOrg.objects.get(id = int(org_id))

        # 查询课程是否已经收藏
       has_fav = u'收藏'
       if request.user.is_authenticated():
           if UserFavorite.objects.filter(fav_id=course_org.id, user=request.user, fav_type=2):
               has_fav = u'已收藏'

       # 通过外键取出所有课程，在demo表中取出所有以CourseOrg为外键的数据
       all_demo = course_org.demo_set.all()[:3]
       all_teacher = course_org.teacher_set.all()[:1]
       return  render(request,'org-detail-homepage.html',{
           'all_demo': all_demo,
           'all_teacher': all_teacher,
           'course_org': course_org,
           'current_page': current_page,
           'has_fav': has_fav,
       })


class OrgCourseView(View):
    def get(self,request,org_id):

        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_demo = course_org.demo_set.all()

        # 查询课程是否已经收藏
        has_fav = u'收藏'
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(fav_id=course_org.id, user=request.user, fav_type=2):
                has_fav = u'已收藏'

        # 对机构课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_demo,8, request=request)
        page_demo = p.page(page)


        course_nums = all_demo.count()
        return render(request, 'org-detail-course.html', {
            'all_demo': page_demo,
            'course_org': course_org,
            'course_nums': course_nums,
            'current_page': current_page,
            'has_fav': has_fav,
        })


class OrgDescView(View):

    def get(self,request,org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))

        # 查询课程是否已经收藏
        has_fav = u'收藏'
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(fav_id=course_org.id, user=request.user, fav_type=2):
                has_fav = u'已收藏'

        return render(request,'org-detail-desc.html',{
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class OrgTeacherView(View):

    def get(self, request, org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teacher = course_org.teacher_set.all()

        # 查询课程是否已经收藏
        has_fav = u'收藏'
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(fav_id=course_org.id, user=request.user, fav_type=2):
                has_fav = u'已收藏'

        return render(request, 'org-detail-teachers.html', {
            'current_page': current_page,
            'all_teacher': all_teacher,
            'course_org': course_org,
            'has_fav': has_fav,

        })


class AddOrgFavView(View):

    # 用户收藏  用户取消收藏  ajax
    def post(self,request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type',0)

        if not request.user.is_authenticated():
            # 判断用户登陆状态，未登录则放回json，并转跳登陆页面
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')

        exist_records = UserFavorite.objects.filter(fav_id = int(fav_id),user = request.user,fav_type = int(fav_type))
        if exist_records:
            # 如果记录已经存在,则表示用户取消收藏
            exist_records.delete()
            return HttpResponse('{"status":"success","msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success","msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail","msg":"收藏出错"}',content_type='application/json')


