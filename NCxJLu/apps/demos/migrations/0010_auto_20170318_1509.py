# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demos', '0009_auto_20170316_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='teacher_tell',
            field=models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='\u8001\u5e08\u544a\u8bc9\u4f60'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='you_need_know',
            field=models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='\u4f60\u9700\u8981\u77e5\u9053'),
        ),
    ]
