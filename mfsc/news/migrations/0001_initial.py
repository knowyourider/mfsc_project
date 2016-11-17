# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-17 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=32, unique=True, verbose_name='Project short name')),
                ('title', models.CharField(max_length=128)),
                ('subtitle', models.CharField(blank=True, default='', max_length=128)),
                ('body_text', models.TextField(blank=True, default='')),
                ('posted', models.DateField(blank=True, null=True, verbose_name='Date posted')),
                ('is_active', models.BooleanField(default=False)),
                ('on_homepage', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['posted'],
            },
        ),
    ]
