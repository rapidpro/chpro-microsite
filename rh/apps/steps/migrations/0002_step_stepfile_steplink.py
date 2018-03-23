# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-23 13:03
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion
import djangocms_link.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('steps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='steps_step', serialize=False, to='cms.CMSPlugin')),
                ('body', models.TextField(verbose_name='body')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='StepFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('tools', 'Tools'), ('examples', 'Examples')], max_length=32)),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step_files', to='steps.Step')),
            ],
        ),
        migrations.CreateModel(
            name='StepLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_style', models.CharField(choices=[('button', 'Button'), ('link', 'Link')], default='button', max_length=10)),
                ('link_text', models.CharField(blank=True, max_length=64, verbose_name='Link Text')),
                ('external_link', models.URLField(blank=True, help_text='Provide a valid URL to an external website.', max_length=2040, validators=[djangocms_link.validators.IntranetURLValidator(intranet_host_re=None)], verbose_name='External link')),
                ('category', models.CharField(choices=[('tools', 'Tools'), ('examples', 'Examples')], max_length=32)),
                ('internal_link', cms.models.fields.PageField(blank=True, help_text='If provided, overrides the external link.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page', verbose_name='Internal link')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step_links', to='steps.Step')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
