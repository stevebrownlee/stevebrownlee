# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170822_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='keywords',
            field=models.CharField(max_length=155),
        ),
    ]
