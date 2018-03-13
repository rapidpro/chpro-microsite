from cms.plugin_base import CMSPluginBase
from django.core.exceptions import ValidationError
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

    def clean(self):
        super().clean()
        if self.get_link() and not self.link_text:
            raise ValidationError({'link_text':'When adding a Link, you need to provide a display text for the it'})


class IconCard(Block):
    icon = FilerImageField(blank=True, null=True)


# ------------------------------------------------------------------------------
# CMS Plugin/Admin
# ------------------------------------------------------------------------------
class HeroPlugin(BlockPlugin):
    name = 'Hero (Simple)'
    module = 'Content'
    model = Hero
    render_template = "cms_plugins/content/hero.html"
    child_classes = (
        'LinkPlugin',
        'FilerImagePlugin',
    )

    fieldsets = (
        ('Content', {
            'fields': BlockMixin._admin_fields,
        }),
    )


class ComplexHeroPlugin(BlockPlugin):
    name = 'Hero (Complex)'
    module = 'Content'
    model = Hero
    render_template = "cms_plugins/content/hero.html"
    child_classes = (
        'CardPlugin',
    )
    disable_child_plugins = False

    fieldsets = (
        ('Content', {
            'fields': BlockMixin._admin_fields + ('image', 'style'),
        }),
    )


class SectionTextPlugin(BlockPlugin):
    name = 'Section + Text'
    module = 'Content'
    model = Block
    child_classes = (
        'LinkPlugin',
        'FilerImagePlugin',
    )
    render_template = "cms_plugins/content/section.html"
    fieldsets = (
        BlockMixin._admin_fieldset,
        Linkable._admin_fieldset,
    )


class SectionCardsPlugin(BlockPlugin):
    name = 'Section + Cards'
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
    disable_child_plugins = False


class StandaloneCardListPlugin(CMSPluginBase):
    name = 'Standalone Card List'
    module = 'Content'
    render_template = 'cms_plugins/content/render_children.html'
    allow_children = True
    child_classes = (
        'CardPlugin',
    )


class CardPlugin(BlockPlugin):
    name = 'Icon Card'
    module = 'Content'
    model = IconCard
    parent_classes = (
        'SectionPlugin',
    )
    render_template = "cms_plugins/content/card.html"
    fieldsets = (
        ('Icon', {
            'fields': ['icon',],
        }),
        BlockMixin._admin_fieldset,
        Linkable._admin_fieldset,
    )


plugin_pool.register_plugin(HeroPlugin)
plugin_pool.register_plugin(ComplexHeroPlugin)
plugin_pool.register_plugin(SectionTextPlugin)
plugin_pool.register_plugin(SectionCardsPlugin)
plugin_pool.register_plugin(StandaloneCardListPlugin)
plugin_pool.register_plugin(CardPlugin)
