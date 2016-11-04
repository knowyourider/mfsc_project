# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-04 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
        ('plan', '0015_auto_20161104_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='organizations',
            field=models.ManyToManyField(blank=True, to='resources.Organization', verbose_name='Organizations related to this action'),
        ),
    ]
