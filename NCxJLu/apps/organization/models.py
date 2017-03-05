# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):

    city = models.CharField(max_length=100,verbose_name=u'城市')
    desc = models.CharField(max_length=100,verbose_name=u'城市描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.city


class CourseOrg(models.Model):

    name = models.CharField(max_length=100,verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')
    categroy = models.CharField(verbose_name=u'机构类别',max_length=100,choices=(('pxjg',u'培训机构'),('gr',u'个人'),('gx',u'高校')),default='gr')
    click_num = models.IntegerField(default=0,verbose_name=u'点击数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(upload_to="org/%Y/%m",verbose_name=u'封面图片', max_length=200)
    address = models.CharField(max_length=100,verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict,verbose_name=u'所在城市')
    add_time = models.DateTimeField(default=datetime.now)
    index = models.IntegerField(default=999,verbose_name=u'排序')
    has_auth = models.BooleanField(verbose_name=u'是否认证', default=False)
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    couser_num = models.IntegerField(default=0, verbose_name=u'课程数')

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Teacher(models.Model):

    org = models.ForeignKey(CourseOrg,verbose_name=u'所属机构')
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name=u'教师头像', max_length=200,null=True,blank=True)
    name = models.CharField(max_length=100, verbose_name=u'教师名称')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=200, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=200, verbose_name=u'工作职位')
    point = models.CharField(max_length=100,verbose_name=u'教学特点')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏数')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
