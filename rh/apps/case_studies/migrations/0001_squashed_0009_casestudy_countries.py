# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 22:19
from __future__ import unicode_literals

import autoslug.fields
import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import filer.fields.image


class Migration(migrations.Migration):

    replaces = [('case_studies', '0001_initial'), ('case_studies', '0002_auto_20180321_1636'), ('case_studies', '0003_casestudy_use_cases'), ('case_studies', '0004_auto_20180404_0612'), ('case_studies', '0005_auto_20180405_0120'), ('case_studies', '0006_auto_20180409_0403'), ('case_studies', '0007_casestudy_last_modified'), ('case_studies', '0008_casestudy_lead_content'), ('case_studies', '0009_casestudy_countries')]

    initial = True

    dependencies = [
        ('content', '0011_block_style'),
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=128)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=128, populate_from='heading', unique=True)),
                ('published', models.BooleanField(default=False, help_text='Indicates if this Case Study is pubilc or still a draft.', verbose_name='Published')),
                ('featured_image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Featured Image')),
                ('main_content', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_case_study', slotname='case_study_main_content', to='cms.Placeholder', verbose_name='Case Study Main Content')),
                ('sidebar_content', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sidebar_case_study', slotname='case_study_sidebar_content', to='cms.Placeholder', verbose_name='Case Study Sidebar Content')),
                ('stats_content', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stats_case_study', slotname='case_study_stats_content', to='cms.Placeholder', verbose_name='Case Study Stats Content')),
                ('use_cases', models.ManyToManyField(to='cms.Page')),
                ('region', models.CharField(choices=[('americas', 'The Americas and Caribbean'), ('europe-asia-c', 'Europe and Central Asia'), ('pacific-asia-e', 'East Asia and the Pacific'), ('africa-e-s', 'Eastern and Southern Africa'), ('middle-east-africa', 'Middle East and North Africa'), ('asia-s', 'South Asia'), ('africa-w-c', 'West and Central Africa')], max_length=20)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('lead_content', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_case_study', slotname='case_study_lead_content', to='cms.Placeholder', verbose_name='Case Study Lead Content')),
                ('countries', django_countries.fields.CountryField(max_length=746, multiple=True)),
            ],
            options={
                'verbose_name_plural': 'Case Studies',
            },
        ),
    ]
