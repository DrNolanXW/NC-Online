# -*- coding: utf-8 -*-
__author__ = 'wx'
__date__ = '17-2-10 下午 4:54'

from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from NCxJLu.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str


def send_register_email(email,send_type='register'):
    email_record = EmailVerifyRecord()
    random_code =random_str(16)
    email_record.email = email
    email_record.send_type = send_type
    email_record.code = random_code
    email_record.save()

    email_title = ''
    email_bady = ''

    if send_type == 'register':
        email_title = u'NC科技注册激活链接'
        email_bady = u'请点击下面链接激活账号:http://127.0.0.1:8000/active/{0}'.format(random_code)
        #setting配置发送参数
        send_status = send_mail(email_title,email_bady,EMAIL_FROM,[email])
        if send_status :
            pass
    elif send_type == 'forget':
        email_title = u'NC科技密码重置链接'
        email_bady = u'请点击下面重置密码:http://127.0.0.1:8000/reset/{0}'.format(random_code)
        # setting配置发送参数
        send_status = send_mail(email_title, email_bady, EMAIL_FROM, [email])
        if send_status:
            pass



