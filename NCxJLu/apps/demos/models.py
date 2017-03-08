# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from organization.models import CourseOrg

# Create your models here.


class Demo(models.Model):
    Course_Org = models.ForeignKey(CourseOrg,verbose_name=u'课程机构',null=True,blank=True)
    name = models.CharField(max_length=100,verbose_name=u'案例名')
    desc = models.CharField(max_length=1000,verbose_name=u'案例描述')
    detail = models.TextField(verbose_name=u'案例详情')
    degree = models.CharField(verbose_name=u'难度',choices=(('cj',u'初级'),('zj',u'中级'),('gj',u'高级')),max_length=6)
    learn_time = models.IntegerField(default=0,verbose_name=u'学习时长')
    students = models.IntegerField(default=0,verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0,verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='image/%Y/%m',verbose_name=u'视频封面',max_length=100,null=True,blank=True)
    click_num = models.IntegerField(verbose_name=u'点击数',default=0)
    category = models.CharField(max_length=100,verbose_name=u'课程类别',null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'案例'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def get_zj_num(self):
        # 获取章节数
        return self.lesson_set.all().count()

    def get_learn_user(self):
        # 获取学习课程用户
        return  self.usercourse_set.all()[:5]


# Demo和Lesson为1对多关系，采用外键形式建立表
class Lesson(models.Model):
    demo = models.ForeignKey(Demo,verbose_name=u'案例')
    name = models.CharField(max_length=100,verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name


# Lesson和Video为1对多关系，采用外键形式建立表
class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name


# Demo和DemoResource为1对多关系，采用外键形式建立表
class DemoResource(models.Model):
    demo = models.ForeignKey(Demo,verbose_name='案例')
    name = models.CharField(max_length=100, verbose_name='视频资源名')
    downlaod = models.FileField(upload_to='demo/resource/%Y/%m',verbose_name=u'资源文件',max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'案例资源'
        verbose_name_plural = verbose_name



