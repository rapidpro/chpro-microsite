# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-08 22:57
from __future__ import unicode_literals

from django.db import migrations
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    IconCard = apps.get_model('content.IconCard')
    for card in IconCard.objects.filter(slug=None):
        card.slug = slugify(card.title)
        card.save()


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0022_iconcard_slug'),
    ]

    operations = [
        migrations.RunPython(
            populate_slugs, reverse_code=migrations.RunPython.noop)
    ]