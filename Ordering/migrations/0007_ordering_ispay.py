# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-25 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordering', '0006_auto_20180325_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordering',
            name='ispay',
            field=models.BooleanField(default=False),
        ),
    ]
