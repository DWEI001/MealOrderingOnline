# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-06 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180306_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('nick_name', models.CharField(default='游客', max_length=50, verbose_name='昵称 ')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6)),
                ('address', models.CharField(default='', max_length=100)),
                ('mobile', models.CharField(max_length=11)),
                ('image', models.ImageField(default='image/user/default', upload_to='image/user/%Y%m')),
            ],
            options={
                'verbose_name_plural': '用户信息',
                'verbose_name': '用户信息',
            },
        ),
        migrations.RemoveField(
            model_name='userporfile',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userporfile',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='UserPorfile',
        ),
    ]
