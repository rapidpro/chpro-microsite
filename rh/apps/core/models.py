from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.fields import PageField
from djangocms_link.validators import IntranetURLValidator
from djangocms_text_ckeditor.cms_plugins import TextPlugin

from djangocms_text_ckeditor.models import AbstractText

from model_utils import Choices

HOSTNAME = getattr(
    settings,
    'DJANGOCMS_LINK_INTRANET_HOSTNAME_PATTERN',
    None
)


class Linkable(models.Model):
    LINK_STYLE_CHOICES = Choices(
        ('button', 'Button'),
        ('link', 'Link'),
    )

    url_validators = [IntranetURLValidator(intranet_host_re=HOSTNAME), ]

    link_style = models.CharField(choices=LINK_STYLE_CHOICES, max_length=10, default=LINK_STYLE_CHOICES.button)
    link_text = models.CharField(_('Link Text'), max_length=64, blank=True)
    external_link = models.URLField(
        verbose_name=_('External link'),
        blank=True,
        max_length=2040,
        validators=url_validators,
        help_text=_('Provide a valid URL to an external website.'),
    )
    internal_link = PageField(
        verbose_name=_('Internal link'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('If provided, overrides the external link.'),
    )

    def get_link(self):
        link = None
        if self.internal_link:
            ref_page = self.internal_link
            link = ref_page.get_absolute_url()

            if ref_page.site_id != getattr(self.page, 'site_id', None):
                ref_site = Site.objects._get_site_by_id(ref_page.site_id)
                link = '//{}{}'.format(ref_site, link)
        elif self.external_link:
            link = self.external_link

        return link

    _admin_fields = ('link_text', ('external_link', 'internal_link'), 'link_style')
    _admin_fieldset = ('Link', {
        'fields': _admin_fields
    })

    class Meta:
        abstract = True


class BlockMixin(AbstractText):
    title = models.CharField(_('Title'), max_length=256)

    _admin_fields = ('title', 'body',)
    _admin_fieldset = ('Content', {
        'fields': _admin_fields,
    })

    class Meta:
        abstract = True

    def clean_plugins(self):
        """
        Don't remove any plugins.
        """
        # AbstractText removes child plugins that aren't in the text
        # itself. We don't want to do this.


class BlockPlugin(TextPlugin):

    # This is necessary because TextPlugin overrides the context.
    # Using {{ instance }} is consistent with the rest of the plugins
    def render(self, context, instance, placeholder):
        ctx = super(BlockPlugin, self).render(context, instance, placeholder)
        ctx['instance'] = ctx['object']
        return ctx
