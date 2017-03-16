# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0008_teacher_image'),
        ('demos', '0007_video_learn_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='\u6388\u8bfe\u6559\u5e08'),
        ),
    ]
