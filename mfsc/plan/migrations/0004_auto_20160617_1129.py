# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20160617_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='rec',
            name='related',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='rec',
            name='responsible',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]