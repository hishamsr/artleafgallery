# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_auto_20160611_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artimage',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Category'),
        ),
    ]
