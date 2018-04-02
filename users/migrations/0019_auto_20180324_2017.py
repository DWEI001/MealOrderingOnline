# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-24 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20180320_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '忘记密码'), ('update_email', '修改邮箱')], max_length=10, verbose_name='类型'),
        ),
    ]