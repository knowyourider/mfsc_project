# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-30 00:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_organization_ordinal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['ordinal']},
        ),
    ]
