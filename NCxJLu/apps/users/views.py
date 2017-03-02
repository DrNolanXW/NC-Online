# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password


# Create your views here.
from .models import UserProflie,EmailVerifyRecord
from .forms import LoginForm,RegisterForm,ForgetForm,ModifyPwdForm

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
            send_register_email(email)
            user_profile.save()
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


