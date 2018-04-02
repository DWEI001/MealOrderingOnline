# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-26 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordering', '0007_ordering_ispay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordering',
            old_name='ispay',
            new_name='is_pay',
        ),
        migrations.AddField(
            model_name='ordering',
            name='content',
            field=models.TextField(default='', verbose_name='留言'),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='address',
            field=models.CharField(default='', max_length=50, verbose_name='收货地址'),
        ),
    ]