# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.template.defaulttags import register

from rh.apps.icons.models import CustomSVGIcon


@register.simple_tag()
def get_uploaded_icon(name):
    """
    Loads a custom icon by its prefixed name.
    """
    try:
        pk = int(name.replace(CustomSVGIcon.ICON_PREFIX, ''))
        icon = CustomSVGIcon.objects.get(pk=pk)
        return icon
    # Somebody tinkered with the url name
    except ValueError:
        return None
    # Icon was deleted
    except CustomSVGIcon.DoesNotExist:
        return None


@register.assignment_tag
def get_uploaded_icon_list():
    """
    Returns an object of all Custom Uploaded SVG Icons.
    """
    icons = {}
    for icon in CustomSVGIcon.objects.all():
        icons[icon.prefixed_id] = icon.svg.url
    return json.dumps(icons)
