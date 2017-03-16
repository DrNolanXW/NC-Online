# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-7 下午 4:04'
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from operation.models import UserFavorite,CourseComments,UserCourse
from utils.mixin_utils import *


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

        tag = demo.tag
        if tag:
            relate_tag = Demo.objects.filter(tag=tag)[:1]
        else:
            # 传递数组
            relate_tag = []

        return render(request,'course-detail.html',{
            'demo': demo,
            'relate_tag': relate_tag,
        })


class AddFavView(View):
    # 收藏课程
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            # 判断用户登陆状态，未登录则放回json，并转跳登陆页面
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')

        exist_records = UserFavorite.objects.filter(fav_id=int(fav_id), user=request.user, fav_type=int(fav_type))
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
                return HttpResponse('{"status":"fail","msg":"收藏出错"}', content_type='application/json')


class CouserVideoView(LoginRequiredMixin,View):

    def get(self,request,demo_id):
        demo = Demo.objects.get(id=int(demo_id))
        user_demos = UserCourse.objects.filter(demo=demo)

        # 查看用户是否关联，如果未关联则建立连接
        user_courses = UserCourse.objects.filter(user=request.user,demo =demo)
        if not user_courses:
            user_course = UserCourse(user=request.user,demo =demo)
            user_course.save()

        # 取出所有学习该课程的用户，然后查询这些用户学过的课程
        user_ids = [user.id for user in user_demos]     # user.id的数组
        all_user_courses = UserCourse.objects.filter(user_id__in = user_ids)
        course_id = [user_course.id for user_course in all_user_courses] # courser.id的数组
        courses = Demo.objects.filter(id__in=course_id).order_by("-click_num")

        all_resourse = DemoResource.objects.filter(demo=demo)
        return render(request,'course-video.html',{
            'demo':demo,
            'all_resourse':all_resourse,
            'relate_courses':courses,
        })


class CommentsView(LoginRequiredMixin,View):
    def get(self,request,demo_id):
        demo = Demo.objects.get(id=int(demo_id))
        all_resourse = DemoResource.objects.filter(demo=demo)
        all_comment = CourseComments.objects.filter(demo=demo)
        return render(request,'course-comment.html',{
            'demo':demo,
            'all_resourse':all_resourse,
            'all_comment':all_comment,
        })


class AddCommentView(View):
    # 添加评论
    def post(self,request):

        if not request.user.is_authenticated():
            # 判断用户登陆状态，未登录则放回json，并转跳登陆页面
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')

        demo_id = request.POST.get("course_id",0)
        comments = request.POST.get("comments","")
        if demo_id>0 and comments :
            course_comments = CourseComments()
            demo = Demo.objects.get(id = int (demo_id))
            course_comments.demo = demo
            course_comments.comment = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success","msg":"评论成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"评论失败"}',content_type='application/json')


