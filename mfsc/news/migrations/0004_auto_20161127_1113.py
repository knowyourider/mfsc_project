# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-27 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsitem_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='credit',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Image credit'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='news_image',
            field=models.ImageField(blank=True, upload_to='news'),
        ),
    ]
