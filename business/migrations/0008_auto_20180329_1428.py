# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-29 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0007_auto_20180329_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='激活状态'),
        ),
        migrations.AlterField(
            model_name='business',
            name='bstatus',
            field=models.BooleanField(default=False, verbose_name='在线状态'),
        ),
    ]