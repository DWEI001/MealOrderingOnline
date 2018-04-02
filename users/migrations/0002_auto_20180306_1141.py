# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-06 03:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='验证码')),
                ('emil', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '忘记密码')], max_length=10)),
                ('send_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
        migrations.AlterField(
            model_name='userporfile',
            name='image',
            field=models.ImageField(default='image/user/default', upload_to='image/user/%Y%m'),
        ),
        migrations.AlterField(
            model_name='userporfile',
            name='nick_name',
            field=models.CharField(default='游客', max_length=50, verbose_name='昵称 '),
        ),
    ]