from django.db import models
from django.contrib import admin

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

from djangocms_text_ckeditor.fields import HTMLField
from rh.apps.icons.models import IconMixin


# ------------------------------------------------------------------------------
# Models
# ------------------------------------------------------------------------------

class MetaAttributesAsPlugin(CMSPlugin):
    class Meta:
        verbose_name = 'Meta Attributes as Plugin'
        verbose_name_plural = 'Meta Attributes as Plugin'


class MetaAttributes(PageExtension, IconMixin):
    description = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Meta Attributes'
        verbose_name_plural = 'Meta Attributes'


extension_pool.register(MetaAttributes)
