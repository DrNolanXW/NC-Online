# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProflie
from demos.models import Demo

# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=100,verbose_name=u'姓名')
    mobile = models.CharField(max_length=11,verbose_name=u'手机')
    course_name = models.CharField(max_length=100,verbose_name=u'课程名称')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    # 课程评论
    user = models.ForeignKey(UserProflie,verbose_name=u'用户')
    demo = models.ForeignKey(Demo,verbose_name=u'课程')
    comment = models.CharField(max_length=500,verbose_name=u'用户评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProflie,verbose_name=u'用户')
    fav_id = models.IntegerField(default=0,verbose_name=u'数据id')
    fav_type = models.IntegerField(choices=((1,u'课程'),(2,u'课程机构'),(3,u'讲师')),default=1,verbose_name='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    #消息系统
    user = models.IntegerField(default=0,verbose_name=u'接收用户')
    message = models.CharField(max_length=500,verbose_name=u'消息内容')
    #以has开头的布尔类型
    has_read = models.BooleanField(default=False,verbose_name=u'消息是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'消息时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProflie, verbose_name=u'用户')
    demo = models.ForeignKey(Demo, verbose_name=u'课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'学习时间')

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.user.name







