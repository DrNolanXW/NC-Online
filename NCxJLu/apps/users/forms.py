# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-2-10 下午 2:04'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # username 不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误'})


class ModifyPwdForm(forms.Form):
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)



