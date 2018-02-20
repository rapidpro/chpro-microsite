# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='link_style',
            field=models.CharField(choices=[('button', 'Button'), ('link', 'Link')], default='link', max_length=10),
        ),
        migrations.AlterField(
            model_name='block',
            name='link_text',
            field=models.CharField(blank=True, max_length=64, verbose_name='Link Text'),
        ),
    ]
