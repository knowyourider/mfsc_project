# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-16 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=32, unique=True, verbose_name='Menu short name')),
                ('title', models.CharField(max_length=128)),
                ('menu_blurb', models.TextField(blank=True, default='', verbose_name='About this menu')),
            ],
        ),
    ]
