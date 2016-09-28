# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-19 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0008_auto_20160619_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=16, unique=True, verbose_name='Tag short name')),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]