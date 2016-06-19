# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-19 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0007_auto_20160617_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='background',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='action',
            name='metrics',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='action',
            name='progress',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='goal',
            name='background',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='goal',
            name='metrics',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='goal',
            name='progress',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='goal',
            name='related',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='rec',
            name='background',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='rec',
            name='metrics',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='rec',
            name='progress',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='action',
            name='related',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='goal',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='goal',
            name='responsible',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
