# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-13 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180312_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='status',
            field=models.BooleanField(choices=[('1', '在线'), ('0', '离线')], default='0'),
        ),
    ]
