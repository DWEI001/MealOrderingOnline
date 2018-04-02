# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-06 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180306_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailverifyrecord',
            old_name='emil',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='手机号'),
        ),
    ]