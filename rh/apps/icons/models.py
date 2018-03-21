"""
The Icon Module displays one or more icon images accompanied by heading and body text.
The module may optionally include an overarching heading above the icons, and each icon may
include a call-to-action button that enables the user to navigate or take action.
"""
from logging import getLogger

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.six import python_2_unicode_compatible

from .base import IconField

logger = getLogger(__file__)


# ------------------------------------------------------------------------------
# Models
# ------------------------------------------------------------------------------

@python_2_unicode_compatible
class CustomSVGIcon(models.Model):
    """
    Custom SVG Icons which are displayed along the SVG Icon sprite.
    """
    # Custom icons have use this name schema to indicate they are uploaded
    # rather than an icon from the sprite batch.
    ICON_PREFIX = 'uploaded-svg-file-'

    name = models.CharField('Name', max_length=50)
    svg = models.FileField('SVG Icon File', upload_to='svg_icons/',
        help_text='Please check the SVG Icon source for malicious code '
                   'before uploading it.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Custom SVG Icon'
        verbose_name_plural = 'Custom SVG Icons'
        ordering = ('name',)

    @property
    def prefixed_id(self):
        return '{}{}'.format(self.ICON_PREFIX, self.pk)

    def get_absolute_url(self):
        return reverse('custom-svg', kwargs={'pk': self.pk})

    def read(self):
        """
        Reads the file content of the given SVG file and returns it as is.
        """
        try:
            self.svg.seek(0)
            return self.svg.read()
        except Exception as e:  # Should be IOError only but lets catch it all
            if settings.DEBUG:
                logger.error("Could not read SVG Icon")
                logger.exception(e)
            return ''


# ------------------------------------------------------------------------------
# CMS Plugin/Admin
# ------------------------------------------------------------------------------
class IconMixin(models.Model):
    """
    Our very own Icon model which displays an icon from an svg file.

    This is the abstract Base class, we have dedicated models and plugins below.
    """

    # Holds the icon name itself. Icon name is either just the indicator of
    # our SVG Icon sprite, or starts with `uploaded-svg-file-` indicating
    # it's a custom uploaded SVG delivered by the model above.
    svg_icon = IconField('SVG Icon', max_length=100, blank=True, null=True)

    _admin_fields = ['svg_icon']
    _admin_fieldset = ('Icon', {
        'fields': _admin_fields,
    })

    class Meta:
        abstract = True

