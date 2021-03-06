# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 08:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('content', '0006_auto_20180320_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCard',
            fields=[
                ('block_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, primary_key=True, serialize=False, to='content.Block')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.block',),
        ),
    ]
