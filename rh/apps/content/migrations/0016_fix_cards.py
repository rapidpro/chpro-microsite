# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-04 22:51
from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def fix(apps, schema_editor):
    IconCard = apps.get_model('content.IconCard')
    PhotoCard = apps.get_model('content.PhotoCard')
    fields = (
        'title', 'link_style', 'link_text', 'external_link', 'internal_link',
        'body')
    cards = chain(IconCard.objects.iterator(), PhotoCard.objects.iterator())
    for card in cards:
        for field in fields:
            setattr(card, 'fix_{}'.format(field), getattr(card, field))
        card.fix_cmsplugin_ptr = card.block_ptr.cmsplugin_ptr
        card.save()


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_auto_20180404_2250'),
    ]

    operations = [
        migrations.RunPython(fix, reverse_code=migrations.RunPython.noop)
    ]
