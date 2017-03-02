# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# 记录用户相关的信息
class UserProflie(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name=u'昵称',default='')
    birday=models.DateField(verbose_name=u'生日',null=True,blank=True)
    address=models.CharField(max_length=500,default=u'1')
    gender=models.CharField(max_length=10,choices=(('male',u'男'),('female',u'女')),default=u'男')
    mobile=models.CharField(max_length=11,null=True,blank=True)
    image=models.ImageField(upload_to='image/%Y/%m',default='image/default.png')

    class Meta:
        verbose_name=u"用户信息"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username


# 邮箱验证数据表
class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=30,verbose_name=u"验证码")
    email=models.EmailField(max_length=100,verbose_name=u'邮箱')
    send_type=models.CharField(choices=(("register",u'注册'),("forget",u"找回密码")),max_length=10,verbose_name=u'验证码类型')
    # 注意datetime.now()去掉括号
    send_time=models.DateTimeField(default=datetime.now,verbose_name=u'发送时间')

    class Meta:
        verbose_name=u'邮箱验证码'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.email,self.code)


# 首页轮播图设置
class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name=u'标题')
    image=models.ImageField(upload_to='banner/%Y/%m',verbose_name=u'轮播图')
    url=models.URLField(max_length=200,verbose_name=u'访问地址')
    index=models.IntegerField(default=100,verbose_name=u'顺序')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'轮播图'
        verbose_name_plural=verbose_name






