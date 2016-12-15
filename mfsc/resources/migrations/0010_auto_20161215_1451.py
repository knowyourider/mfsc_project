# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-15 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0009_resourcepdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcepdf',
            name='category',
            field=models.IntegerField(choices=[(0, 'no category'), (1, 'category 1'), (2, 'category 2'), (3, 'category 3')], default=0),
        ),
        migrations.AddField(
            model_name='resourcepdf',
            name='handy_label',
            field=models.CharField(default='handy default', max_length=64),
            preserve_default=False,
        ),
    ]
