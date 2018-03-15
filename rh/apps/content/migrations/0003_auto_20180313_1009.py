# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-13 10:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('content', '0002_auto_20180220_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_hero', serialize=False, to='cms.CMSPlugin')),
                ('body', models.TextField(verbose_name='body')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('style', models.CharField(choices=[('clean', 'Clean')], default='clean', max_length=32)),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='heading',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='heading',
            name='image',
        ),
        migrations.DeleteModel(
            name='Heading',
        ),
    ]