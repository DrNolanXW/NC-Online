# -*- coding: utf-8 -*-
"""NCxJLu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
# 处理静态文件
from django.views.generic import TemplateView
from users.views import LoginView
from users.views import RegisterView
from users.views import ActiveUserView
from users.views import ForgetPwdView
from users.views import ResetView
from users.views import ModifyPwdView
from  organization.views import OrgListView

from NCxJLu.settings import MEDIA_ROOT

import xadmin


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    # 根目录前面不加‘/’
    url(r'^login/',LoginView.as_view(),name='login'),

    url(r'^index/$',TemplateView.as_view(template_name='index.html'),name='index'),

    url(r'^$',TemplateView.as_view(template_name='page.html'),name='page'),

    url(r'^register/',RegisterView.as_view(),name='register'),

    url(r'^captcha/', include('captcha.urls')),

    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name='active'),

    url(r'^forgetpwd/$', ForgetPwdView.as_view(),name='forgetpwd'),

    url(r'^reset/(?P<reset_code>.*)/$',ResetView.as_view(),name='reset'),

    url(r'^modify_pwd/$', ModifyPwdView.as_view(),name='modify_pwd'),

    #课程机构首页
    url(r'^org_list/', include('organization.urls',namespace='org_list')),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',serve, {"document_root":MEDIA_ROOT}),

    # 课程相关
    url(r'^course_list/', include('demos.urls', namespace='course_list')),

    # 讲师相关
    url(r'^teacher/', include('organization.urls', namespace='teacher_list')),

    # 用户中心
    url(r'^user/', include('users.urls', namespace='user')),
]
