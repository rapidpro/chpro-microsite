# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-23 13:10
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('steps', '0002_step_stepfile_steplink'),
    ]

    operations = [
        migrations.AddField(
            model_name='stepfile',
            name='file',
            field=filer.fields.file.FilerFileField(default=1, on_delete=django.db.models.deletion.CASCADE, to='filer.File'),
            preserve_default=False,
        ),
    ]