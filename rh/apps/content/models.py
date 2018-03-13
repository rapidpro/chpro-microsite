from django.db import models

from cms.plugin_pool import plugin_pool

from filer.fields.image import FilerImageField
from model_utils import Choices

from rh.apps.core.models import BlockMixin, Linkable, BlockPlugin


# ------------------------------------------------------------------------------
# Models
# ------------------------------------------------------------------------------
class Hero(BlockMixin):
    STYLE_CHOICES = Choices(
        ('clean', 'Clean'),
    )

    image = FilerImageField(blank=True, null=True)
    style = models.CharField(choices=STYLE_CHOICES, max_length=32, default=STYLE_CHOICES.clean)


class Block(BlockMixin, Linkable):
    def __str__(self):
        return self.title


# ------------------------------------------------------------------------------
# CMS Plugin/Admin
# ------------------------------------------------------------------------------
class HeroPlugin(BlockPlugin):
    name = 'Hero Plugin'
    module = 'Content'
    model = Hero
    render_template = "cms_plugins/content/heading.html"

    fieldsets = (
        ('Content', {
            'fields': BlockMixin._admin_fields + ('image', 'style'),
        }),
    )


class SectionPlugin(BlockPlugin):
    name = 'Section Plugin'
    module = 'Content'
    model = Block
    allow_children = True
    child_classes = (
        'CardPlugin',
    )
    render_template = "cms_plugins/content/section.html"
    fieldsets = (
        BlockMixin._admin_fieldset,
        Linkable._admin_fieldset,
    )



class CardPlugin(BlockPlugin):
    name = 'Card Plugin'
    module = 'Content'
    model = Block
    allow_children = True
    parent_classes = (
        'SectionPlugin',
    )
    render_template = "cms_plugins/content/card.html"
    fieldsets = (
        BlockMixin._admin_fieldset,
        Linkable._admin_fieldset,
    )


plugin_pool.register_plugin(HeroPlugin)
plugin_pool.register_plugin(SectionPlugin)
plugin_pool.register_plugin(CardPlugin)
