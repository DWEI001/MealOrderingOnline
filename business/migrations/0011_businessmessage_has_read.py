# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-31 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0010_auto_20180331_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessmessage',
            name='has_read',
            field=models.BooleanField(default=False, verbose_name='是否已读'),
        ),
    ]