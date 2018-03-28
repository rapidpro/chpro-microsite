from cms.models import CMSPlugin
from cms.models.fields import PageField
from cms.plugin_base import CMSPluginBase
from django.core.exceptions import ValidationError
from django.db import models

from cms.plugin_pool import plugin_pool

from filer.fields.image import FilerImageField
from model_utils import Choices

from rh.apps.core.models import BlockMixin, Linkable, BlockPlugin
from rh.apps.icons.models import IconMixin


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
    STYLE_CHOICES = Choices(
        ('default', 'White'),
        ('light', 'Light'),
        ('dark', 'Dark'),
    )
    style = models.CharField(
        choices=STYLE_CHOICES, max_length=32, default=STYLE_CHOICES.default)

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.get_link() and not self.link_text:
            raise ValidationError({'link_text':'When adding a Link, you need to provide a display text for the it'})


class CardGrid(CMSPlugin):
    root = PageField(
        blank=True, null=True,
        help_text='Select a root page to list all of its children as cards. '
                  'If this is left empty, you will have to manually add cards to the grid.')

    def get_published_child_pages(self):
        """
        Returns all child pages of the selected root page which are
        published.
        :return:
        """
        if self.root:
            return self.root.get_children().published()
        return []

    def __str__(self):
        return str(self.root) or f'Manual Card Grid ({self.pk})'


class IconCard(Block, IconMixin):
    pass


class PhotoCard(Block):
    image = FilerImageField(blank=True, null=True)


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
    render_template = "cms_plugins/content/hero_complex.html"
    child_classes = (
        'CardPlugin',
        'ImageCardPlugin',
    )
    allow_children = True
    disable_child_plugins = False

    fieldsets = (
        ('Content', {
            'fields': BlockMixin._admin_fields + ('image', 'style'),
        }),
    )


class AccordionCardPlugin(BlockPlugin):
    name = 'Accordion Card'
    module = 'Content'
    model = PhotoCard
    parent_classes = (
        'FeaturedAccordionPlugin',
    )
    render_template = "cms_plugins/content/accordion_card.html"
    fieldsets = (
        ('Image', {
            'fields': ('image',)
        }),
        BlockMixin._admin_fieldset,
        Linkable._admin_fieldset,
    )


class FeaturedAccordionPlugin(BlockPlugin):
    name = 'Featured (Accordion)'
    module = 'Content'
    model = Hero
    render_template = "cms_plugins/content/accordion.html"
    child_classes = (
        'AccordionCardPlugin',
    )
    allow_children = True
    disable_child_plugins = False

    fieldsets = (
        ('Content', {
            'fields': ('title', 'style',),
        }),
    )


class SectionPlugin(BlockPlugin):
    name = 'Section'
    module = 'Content'
    model = Block
    child_classes = (
        'LinkPlugin',
        'FilerImagePlugin',
    )
    render_template = "cms_plugins/content/section.html"
    fieldsets = (
        ('Style', {'fields': ('style',)}),
        BlockMixin._admin_fieldset,
        Linkable._admin_fieldset,
    )


class SectionCardsPlugin(BlockPlugin):
    name = 'Section + Cards'
    module = 'Content'
    model = Block
    allow_children = True
    disable_child_plugins = False
    child_classes = (
        'CardPlugin',
    )
    render_template = "cms_plugins/content/section.html"
    fieldsets = (
        BlockMixin._admin_fieldset,
        Linkable._admin_fieldset,
    )


class CardGridPlugin(CMSPluginBase):
    name = 'Card Grid'
    module = 'Content'
    model = CardGrid
    render_template = 'cms_plugins/content/card_grid.html'
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
        IconMixin._admin_fieldset,
        BlockMixin._admin_fieldset,
        Linkable._admin_fieldset,
    )


class ImageCardPlugin(BlockPlugin):
    name = 'Photo Card'
    module = 'Content'
    model = PhotoCard
    parent_classes = (
        'ComplexHeroPlugin',
    )
    render_template = "cms_plugins/content/image_card.html"
    fieldsets = (
        ('Image', {
            'fields': ('image',)
        }),
        BlockMixin._admin_fieldset,
        Linkable._admin_fieldset,
    )


plugin_pool.register_plugin(HeroPlugin)
plugin_pool.register_plugin(ComplexHeroPlugin)
plugin_pool.register_plugin(SectionPlugin)
plugin_pool.register_plugin(SectionCardsPlugin)
plugin_pool.register_plugin(CardGridPlugin)
plugin_pool.register_plugin(CardPlugin)
plugin_pool.register_plugin(ImageCardPlugin)
plugin_pool.register_plugin(FeaturedAccordionPlugin)
plugin_pool.register_plugin(AccordionCardPlugin)
