# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.template.defaulttags import register


@register.simple_tag()
def get_full_url(request, url=None):
    """
    Build an absolute uri
    """

    scheme = settings.HTTPS_LINKS and 'https' or 'http'
    host = request.META['HTTP_HOST']

    if not url:
        url = request.path
    else:
        url = '/' + str(url)

    return '{scheme}://{host}{url}'.format(scheme=scheme, host=host, url=url)
