# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-2-9 下午 9:51'

# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-2-8 上午 1:03'

#后台配置放置于此

import xadmin
from xadmin import views

from .models import EmailVerifyRecord
from .models import UserProflie
from .models import Banner

# Register your models here.


class BaseSetting(object):
    # 增加后台主题
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):

    # 修改标题和注脚
    site_title = 'NC XJZH'
    site_footer = 'NC科技'

    # 设置左侧菜单栏样式
    menu_style = 'accordion'



class UserProflieAdmin(object):

    list_display = ['email','nick_name', 'birday','gender','mobile','is_active']
    search_fields = ['email','nick_name','birday','gender','mobile',]
    list_filter = ['nick_name','email', 'birday','gender','mobile',]


class BannerAdmin(object):
    list_display = ['title','url']
    search_fields = ['title','url',]
    list_filter = ['title','url', 'add_time']


class EmailVerifyRecordAdmin(object):
    list_display = ['email','code','send_type','send_time']
    search_fields = ['email','code','send_type']
    list_filter = ['email','code','send_type','send_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(UserProflie,UserProflieAdmin)
xadmin.site.register(Banner,BannerAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)