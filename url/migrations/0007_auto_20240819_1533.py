# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2024-08-19 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0006_auto_20240813_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='old_url',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]