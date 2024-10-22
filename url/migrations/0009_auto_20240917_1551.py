# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2024-09-17 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0008_auto_20240902_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='new_url',
            field=models.CharField(default='', editable=False, max_length=700, verbose_name='Codigo da URL encurtada.'),
        ),
        migrations.AlterField(
            model_name='url',
            name='old_url',
            field=models.CharField(help_text='Digite a URL a ser encurtada.', max_length=100, verbose_name='URL original'),
        ),
    ]
