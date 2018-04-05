# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-04 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_auto_20180404_2333'),
    ]

    operations = [
        migrations.RenameModel(
            'Block', 'Section'
        ),
        migrations.AlterField(
            model_name='section',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_section', serialize=False, to='cms.CMSPlugin'),
        ),
    ]