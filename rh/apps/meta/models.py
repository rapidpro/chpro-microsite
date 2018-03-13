from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase

from cms.plugin_pool import plugin_pool
from djangocms_text_ckeditor.fields import HTMLField

from filer.fields.image import FilerImageField


# ------------------------------------------------------------------------------
# Models
# ------------------------------------------------------------------------------
class MetaAttributes(CMSPlugin):
    description = HTMLField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True)


# ------------------------------------------------------------------------------
# CMS Plugin/Admin
# ------------------------------------------------------------------------------
class MetaAttributesPlugin(CMSPluginBase):
    name = 'Meta Attributes'
    module = 'Meta'
    model = MetaAttributes
    render_template = "cms_plugins/meta/empty.html"

    fieldsets = (
        ('Listing', {
            'fields': ('icon', 'description')
        }),
    )


plugin_pool.register_plugin(MetaAttributesPlugin)
