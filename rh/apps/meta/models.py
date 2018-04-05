from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.db import models

from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from rh.apps.icons.models import IconMixin


# ------------------------------------------------------------------------------
# Models
# ------------------------------------------------------------------------------

class MetaAttributes(PageExtension, IconMixin):
    image = FilerImageField(blank=True, null=True)

    lead = HTMLField(
        max_length=256, blank=True, null=True,
        help_text='Short description of the page. Used by the step list plugin.')

    description = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Meta Attributes'
        verbose_name_plural = 'Meta Attributes'


class Pagination(CMSPlugin):
    show_numbers = models.BooleanField(default=True)


# ------------------------------------------------------------------------------
# CMS Plugin/Admin
# ------------------------------------------------------------------------------

class PaginationPlugin(CMSPluginBase):
    name = 'Pagination'
    module = 'Content'
    model = Pagination
    render_template = "cms_plugins/meta/pagination.html"

    fieldsets = (
        ('Content', {
            'fields': ('show_numbers',)
        }),
    )

    def render(self, context, instance, placeholder):
        page = instance.page
        prev_num, next_num = None, None
        for i, sibling in enumerate(page.get_siblings()):
            if sibling == page:
                prev_num = i
                next_num = i + 2
                break
        context.update({
            'prev': page.get_prev_sibling(),
            'next': page.get_next_sibling(),
            'prev_num': prev_num,
            'next_num': next_num,
            'instance': instance,
        })
        return context


extension_pool.register(MetaAttributes)
plugin_pool.register_plugin(PaginationPlugin)
