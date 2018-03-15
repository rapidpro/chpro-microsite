from django.db import models
from django.contrib import admin

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


# ------------------------------------------------------------------------------
# Models
# ------------------------------------------------------------------------------
class MetaAttributesAsPlugin(CMSPlugin):
    class Meta:
        verbose_name = 'Meta Attributes as Plugin'
        verbose_name_plural = 'Meta Attributes as Plugin'


class MetaAttributes(PageExtension):
    description = HTMLField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True)
    plugins = models.ForeignKey(MetaAttributesAsPlugin, null=True, blank=True)

    class Meta:
        verbose_name = 'Meta Attributes'
        verbose_name_plural = 'Meta Attributes'

extension_pool.register(MetaAttributes)

# ------------------------------------------------------------------------------
# CMS Plugin/Admin
# ------------------------------------------------------------------------------
class MetaAttributesInlineAdmin(admin.StackedInline):
    model = MetaAttributes
    extra = 1
    min_num = 1
    max_num = 1


class MetaAttributesPlugin(CMSPluginBase):
    name = 'Meta Attributes'
    module = 'Meta'
    model = MetaAttributesAsPlugin
    render_template = "cms_plugins/meta/empty.html"
    exclude = ['attributes']
    inlines = (MetaAttributesInlineAdmin,)


plugin_pool.register_plugin(MetaAttributesPlugin)
