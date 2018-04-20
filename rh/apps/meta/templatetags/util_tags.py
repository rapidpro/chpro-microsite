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
    host = request.META.get('HTTP_HOST', 'defaulthost.com')

    # removes trailing slash
    if not url:
        url = request.path[:-1]
    # adds slash if you enter a url manually
    else:
        url = '/' + str(url)

    return '{scheme}://{host}{url}'.format(scheme=scheme, host=host, url=url)


@register.simple_tag()
def get_full_host(request):
    """
    Build an url for site host
    """

    scheme = settings.HTTPS_LINKS and 'https' or 'http'
    host = request.META.get('HTTP_HOST', 'defaulthost.com')

    return '{scheme}://{host}'.format(scheme=scheme, host=host)
