# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_auto_20160617_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rec',
            name='description',
            field=models.TextField(),
        ),
    ]