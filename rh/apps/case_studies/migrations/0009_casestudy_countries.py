# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-13 03:57
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('case_studies', '0008_casestudy_lead_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudy',
            name='countries',
            field=django_countries.fields.CountryField(default='', max_length=746, multiple=True),
            preserve_default=False,
        ),
    ]
