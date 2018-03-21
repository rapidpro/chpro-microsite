# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 16:36
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case_studies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudy',
            name='main_content',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_case_study', slotname='case_study_main_content', to='cms.Placeholder', verbose_name='Case Study Main Content'),
        ),
        migrations.AlterField(
            model_name='casestudy',
            name='published',
            field=models.BooleanField(default=False, help_text='Indicates if this Case Study is pubilc or still a draft.', verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='casestudy',
            name='sidebar_content',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sidebar_case_study', slotname='case_study_sidebar_content', to='cms.Placeholder', verbose_name='Case Study Sidebar Content'),
        ),
        migrations.AlterField(
            model_name='casestudy',
            name='stats_content',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stats_case_study', slotname='case_study_stats_content', to='cms.Placeholder', verbose_name='Case Study Stats Content'),
        ),
    ]
