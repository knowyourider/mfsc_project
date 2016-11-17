# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-16 23:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitewide', '0001_initial'),
        ('stories', '0004_auto_20161115_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='menu',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='sitewide.Menu'),
        ),
    ]