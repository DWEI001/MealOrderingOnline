# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-28 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0006_auto_20180326_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuinfo',
            name='menu_type',
            field=models.CharField(default='', max_length=30, verbose_name='菜品类型'),
        ),
    ]
