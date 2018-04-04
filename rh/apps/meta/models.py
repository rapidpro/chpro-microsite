from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

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


extension_pool.register(MetaAttributes)
