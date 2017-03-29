# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,HttpResponseRedirect

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from utils.mixin_utils import LoginRequiredMixin
from .forms import *
from .models import *


# Create your views here.
from .models import UserProflie,EmailVerifyRecord
from .forms import LoginForm,RegisterForm,ForgetForm,ModifyPwdForm
from operation.models import *
from organization.models import *

from utils.email_send import send_register_email


class ActiveUserView(View):
    def get(self,request,active_code):
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        if all_record:
            for record in all_record:
                email = record.email
                user = UserProflie.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request,'active_fail.html')
        return render(request,'login.html')


class RegisterView(View):

    def get(self,request):
        # 获取验证码图片
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email','')
            password = request.POST.get('password','')
            if UserProflie.objects.filter(username = email):
                return render(request,'register.html',{'register_form':register_form,'msg':u'该邮箱已被注册'})
            user_profile = UserProflie()
            user_profile.email = email
            user_profile.username = email
            user_profile.nick_name = email
            user_profile.password = make_password(password)
            user_profile.is_active = False
            user_profile.save()
            send_register_email(email)

            # 写入欢迎注册消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = u'欢迎注册'
            user_message.save()


            return render(request, 'login.html')
        else:
            return render(request,'register.html',{'register_form':register_form})


class LoginView(View):

    def get(self,request):
        return render(request, 'login.html', {})

    def post(self,request):
            # 对前端POST的表单进行验证
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user_name = request.POST.get('username', '')
                pass_word = request.POST.get('password', '')
                user = authenticate(username=user_name, password=pass_word)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return render(request, 'index.html')
                    else:
                        return render(request, 'login.html', {'msg': '该账号未激活'})
                else:
                    return render(request, 'login.html', {'msg': '登陆名或密码出错'})
            else:
                return render(request, 'login.html', {'msg': '登陆名或密码不能为空','login_form':login_form})


class LogoutView(View):
    def get(self,request):
        logout(request)
        # 重定向
        from django.core.urlresolvers import reverse
        return HttpResponseRedirect(reverse("index"))


class CustomBackend(ModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # django储存密码使用密文，所以不用password=password
            user = UserProflie.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# def user_login(request):
#     # 用户登陆
#     if request.method == 'POST':
#         user_name = request.POST.get('username','')
#         pass_word = request.POST.get('password','')
#         print user_name
#         print pass_word
#         user = authenticate(username=user_name,password=pass_word)
#         if user is not None:
#             login(request,user)
#             return  render(request,'index.html')
#         else:
#             return  render(request,'login.html',{'msg':'登陆名或密码错误'})
#     elif request.method == 'GET':
#         return render(request,'login.html',{})


class ForgetPwdView(View):
    def get(self,request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email','')
            send_register_email(email,'forget')
            return render(request,'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetView(View):
    def get(self,request,reset_code):
        all_record = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_record:
            for record in all_record:
                email = record.email
                user = UserProflie.objects.get(email = email)
                return  render(request,'password_reset.html',{'email':email})
        else:
            return render(request,'active_fail.html')
        return render(request,'login.html')


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            email = request.POST.get('email','')
            password = request.POST.get('password','')
            password2 = request.POST.get('password2','')
            print email
            if password != password2:
                return render(request,'password_reset.html',{'email':email,'msg':u'密码不一致'})
            user = UserProflie.objects.get(email=email)
            user.password = make_password(password)
            user.save()
            return render(request,'login.html')
        else:
            email = request.POST.get('email')
            return render(request, 'password_reset.html', {'email': email, 'modify_form':modify_form})


class UserInfoView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'usercenter-info.html')

    def post(self,request):
        # 做修改指明那个实例。用instance =
        user_info_form = UserInfoForm(request.POST,instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')


class UploadImageView(LoginRequiredMixin,View):
    # 用户修改头像
    def post(self,request):
        image_form = UploadImageForm(request.POST,request.FILES)
        if image_form.is_valid():
            image = image_form.cleaned_data['image']
            request.user.image = image
            request.user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


class UpdatePwdView(View):
    # 用户中心修改密码
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            password1 = request.POST.get('password','')
            password2 = request.POST.get('password2','')
            if password1 != password2:
                return HttpResponse('{"status":"fail","msg":"密码不一致"}', content_type='application/json')
            user = request.user
            user.password = make_password(password1)
            user.save()
            return HttpResponse('{"status":"success","msg":"密码修成功"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(modify_form.errors), content_type='application/json')


class MyCouserView(LoginRequiredMixin,View):
    def get(self,request):
        my_couser = UserCourse.objects.filter(user=request.user)
        return render(request,"usercenter-mycourse.html",{
            'my_couser':my_couser,
        })


class MyFavOrgView(LoginRequiredMixin,View):
    def get(self,request):
        org_list = []
        fav_orgs = UserFavorite.objects.filter(user=request.user,fav_type = 2)
        for fav_org in fav_orgs:
            org_id = fav_org.fav_id
            org = CourseOrg.objects.get(id= int(org_id))
            org_list.append(org)
        return render(request,"usercenter-fav-org.html",{
            'org_list':org_list
        })


class MyFavCourseView(LoginRequiredMixin,View):
    def get(self,request):
        course_list = []
        fav_courses = UserFavorite.objects.filter(user=request.user,fav_type = 1)
        for fav_course in fav_courses:
            course_id = fav_course.fav_id
            course = Demo.objects.get(id= int(course_id))
            course_list.append(course)
        return render(request,"usercenter-fav-course.html",{
            'course_list':course_list
        })


class MyFavTeacherView(LoginRequiredMixin,View):
    def get(self,request):
        teacher_list = []
        fav_teachers = UserFavorite.objects.filter(user=request.user,fav_type = 3)
        for fav_org in fav_teachers:
            teacher_id = fav_org.fav_id
            teacher = Teacher.objects.get(id= int(teacher_id))
            teacher_list.append(teacher)
        return render(request,"usercenter-fav-teacher.html",{
            'teacher_list':teacher_list
        })


class MyMessageView(LoginRequiredMixin,View):
    def get(self,request):
        all_message = UserMessage.objects.filter(user = request.user.id)

        # 对机构课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_message, 8, request=request)
        page_message = p.page(page)


        return render(request,"usercenter-message.html",{
            'all_message':page_message
        })


class IndexView(View):
    def get(self,request):
        all_banners = Banner.objects.all()

        return render(request,"index.html",{

        })


def page_no_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html',{})
    response.status_code = 404
    return response


def page_error(request):
    from django.shortcuts import render_to_response
    response = render_to_response('500.html',{})
    response.status_code = 500
    return response