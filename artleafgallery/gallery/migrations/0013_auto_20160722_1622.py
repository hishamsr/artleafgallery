# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-22 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_artimage_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='gallery.Product'),
        ),
    ]
