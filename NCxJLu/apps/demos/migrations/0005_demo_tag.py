# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demos', '0004_auto_20170307_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='tag',
            field=models.CharField(default='', max_length=100, verbose_name='\u8bfe\u7a0b\u6807\u7b7e'),
        ),
    ]
