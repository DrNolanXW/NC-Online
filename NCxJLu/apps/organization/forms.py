# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-3-1 下午 5:23'

import re

from django.forms import ModelForm,forms
from django.forms import ModelForm
from operation.models import UserAsk

class UserAskForm(ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']

    # 定义规则：clean+字段
    def clean_mobile(self):
        # 验证手机号码是否违法
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码违法',code='moblie_invalid')


