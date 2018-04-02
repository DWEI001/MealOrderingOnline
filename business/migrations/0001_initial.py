# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-06 04:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=300, verbose_name='名称')),
                ('bpassword', models.CharField(max_length=100, verbose_name='密码')),
                ('bphone', models.CharField(max_length=11, verbose_name='电话')),
                ('bemail', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('baddress', models.CharField(max_length=300, verbose_name='城市')),
                ('bstatus', models.BooleanField(default=True, verbose_name='状态')),
                ('bimage', models.ImageField(default='image/business/default', upload_to='image/business/%Y%m')),
                ('bcreate_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '商家信息',
                'verbose_name': '商家信息',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='城市名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': '城市信息',
                'verbose_name': '城市信息',
            },
        ),
    ]