# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-26 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20161117_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='news_image',
            field=models.ImageField(blank=True, upload_to='news/testdir'),
        ),
    ]