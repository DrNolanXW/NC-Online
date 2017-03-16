# -*- coding: utf-8 -*-

# 新建app，第一步cmd：python manage.py startapp　ｂｌｏｇ２
# 第二步：打开ｓｅｔｔｉｎｇ．ｐｙ里的INSTALLED_APPS增加ｂｌｏｇ２


# 启动服务器：cmd：pthon manage.py runserver


# 制作数据迁移：
# 第一步: python manage.py makemigrations app名
# 第二步：python manage.py migrate


# 查看sql语句
# python manage.py sqlmigrate 应用名 文件id


# 创建超级用户
# python manage.py createsuperuser
# username:admin
# userpw:123456789a


# 配置应用:
# 第一步:在应用下admin.py中引入自身的models模块
# 第二步：编辑admin.py：admins.site.register(moderls.Article)


# 创建Django工程：
# 在目录下cmd：django—admin startproject 工程名


# django映射到外网：
# 第一步：python manage.py runserver 0.0.0.0:端口号
# 第二步：修改setting文件里的ALLOWED_HOSTS = []添加本地ip地址


# sql的root密码：536095
# 字符集：utf8 -- UTF-8 Unicode
# 排序规则：utf8_general_ci


# 测试app：cmd：python manage.py test -v3 应用名


# django.db.utils.InternalError: 1366:
# http://blog.csdn.net/tianfs/article/details/51775051


# 删除数据库：
# cmd：manage.py migrate your_app_name zero


# 应用放置于app目录:
# setting文件中加入：
# import sys
# sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
# 删除migrations文件夹下的0001_initial.py中所有的app.


# 后台中文，修改setting.py
# 修改为：LANGUAGE_CODE = 'zh-hans'


# 修改后台时区同时要修改setting中的USE_TZ，将其改为false
# 如果设置为True，将默认为UTS时区时间

# 后台全站的配置放置再users.adminx中

#apps配置app显示名称:
#在apps.py中加入：verbose_name = u'用户操作'
#在_init_.py中加入：default_app_config = 'app名.apps.app名Config'

# 配置templates：
# setting.py：'DIRS': [os.path.join(BASE_DIR,"templates")],

# 配置静态文件:
# STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]


# 用邮箱登陆：
# 修改setting里的AUTHENTICATION_BACKENDS = ('users.views.CustomBackend')
# 继承django.contrib.auth.backends import ModelBackend

# 上传文件目录设置
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#在模板中使用{{ MADIE_URL}}
#在setting中添加'django.core.context_porscessors.media',

# 配置上传文件的访问处理函数
# url(r'^media/(?P<path>.*)$',serve, {"document_root":MEDIA_ROOT})

# 分页库：pure_pagination
# pip: django_pure_pagination

# ajax提交非form数据：
#        beforeSend:function(xhr, settings){
#            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
#        },

# {{ demo.get_xxxxxx_display }}
# 用于model中degree设为choices
# 例如 degree = models.CharField(verbose_name=u'难度',choices=(('cj',u'初级'),('zj',u'中级'),('gj',u'高级'))
# {{ demo.get_degree_display }}

#  user_ids = [user.id for user in user_demos]
# 将user_demos中每个user.id添加到user_ids列表中
# all_user_courses = UserCourse.objects.filter(user_id__in = user_ids)
# 用法__in 查询每个等于user_ids元素的值