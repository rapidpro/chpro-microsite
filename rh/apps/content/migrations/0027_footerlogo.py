# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-01 09:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('content', '0026_auto_20180418_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLogo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_footerlogo', serialize=False, to='cms.CMSPlugin')),
                ('alt_text', models.CharField(max_length=100)),
                ('logo', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
