# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-30 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='credit1',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Image 1 credit'),
        ),
        migrations.AddField(
            model_name='project',
            name='credit2',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Image 2 credit'),
        ),
        migrations.AddField(
            model_name='project',
            name='credit3',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Image 3 credit'),
        ),
        migrations.AddField(
            model_name='project',
            name='image1',
            field=models.ImageField(blank=True, upload_to='projects'),
        ),
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, upload_to='projects'),
        ),
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, upload_to='projects'),
        ),
    ]
