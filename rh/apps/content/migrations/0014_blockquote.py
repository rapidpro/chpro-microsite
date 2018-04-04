# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-04 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('content', '0013_rawhtml'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockQuote',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_blockquote', serialize=False, to='cms.CMSPlugin')),
                ('body', models.TextField(verbose_name='body')),
                ('author', models.CharField(max_length=100)),
                ('author_title', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]