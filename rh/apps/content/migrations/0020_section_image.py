# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-05 04:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('content', '0019_remove_orhpaned_sections'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL),
        ),
    ]