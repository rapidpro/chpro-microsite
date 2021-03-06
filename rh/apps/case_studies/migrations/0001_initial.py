# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 15:36
from __future__ import unicode_literals

import autoslug.fields
import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import filer.fields.image
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('heading', models.CharField(max_length=128)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=128, populate_from='heading', unique=True)),
                ('published', models.BooleanField(default=False, help_text='Indicates if this Use Case is pubilc or still a draft.', verbose_name='Published')),
                ('featured_image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Featured Image')),
                ('main_content', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_case_study', slotname='case_study_main_content', to='cms.Placeholder', verbose_name='Use Case Main Content')),
                ('sidebar_content', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sidebar_case_study', slotname='case_study_sidebar_content', to='cms.Placeholder', verbose_name='Use Case Sidebar Content')),
                ('stats_content', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stats_case_study', slotname='case_study_stats_content', to='cms.Placeholder', verbose_name='Use Case Stats Content')),
            ],
            options={
                'verbose_name_plural': 'Case Studies',
            },
        ),
        migrations.CreateModel(
            name='Tagulous_CaseStudy_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='tagulous_casestudy_tags',
            unique_together=set([('slug',)]),
        ),
        migrations.AddField(
            model_name='casestudy',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, help_text='Enter a comma-separated tag string', to='case_studies.Tagulous_CaseStudy_tags', verbose_name='Tags'),
        ),
    ]
