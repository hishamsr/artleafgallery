# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-13 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0013_auto_20160722_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='artimage',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
