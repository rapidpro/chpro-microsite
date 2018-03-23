from django.contrib.admin import StackedInline
from django.db import models

from cms.models import CMSPlugin
from cms.models.fields import PageField
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from filer.fields.file import FilerFileField
from model_utils import Choices

from rh.apps.core.models import BlockMixin, Linkable, BlockPlugin


# ------------------------------------------------------------------------------
# Models
# ------------------------------------------------------------------------------
class StepList(CMSPlugin):
    root = PageField()

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
        return str(self.root)


class Step(BlockMixin):
    CATEGORY_CHOICES = Choices(
        ('tools', 'Tools'),
        ('examples', 'Examples'),
    )

    def __str__(self):
        return self.title

    def copy_relations(self, oldinstance):
        """
        Method is called by django-cms plugin manager once the plugin is saved.
        :see: http://docs.django-cms.org/en/3.2.2/how_to/custom_plugins.html
        """
        for associated_item in oldinstance.step_links.all():
            associated_item.pk = None
            associated_item.plugin = self
            associated_item.save()

        for associated_item in oldinstance.step_files.all():
            associated_item.pk = None
            associated_item.plugin = self
            associated_item.save()


class StepLink(Linkable):
    category = models.CharField(choices=Step.CATEGORY_CHOICES, max_length=32)
    step = models.ForeignKey(Step, related_name='step_links')


class StepFile(models.Model):
    category = models.CharField(choices=Step.CATEGORY_CHOICES, max_length=32)
    file = FilerFileField()
    step = models.ForeignKey(Step, related_name='step_files')


# ------------------------------------------------------------------------------
# CMS Plugin/Admin
# ------------------------------------------------------------------------------
class StepListPlugin(CMSPluginBase):
    name = 'Step List'
    module = 'Steps'
    model = StepList
    render_template = 'cms_plugins/steps/step_list.html'


class StepLinkInline(StackedInline):
    model = StepLink
    min_num = 0
    max_num = 5
    extra = 0
    fieldsets = (
        ('Category', {
            'fields': ('category',)
        }),
        Linkable._admin_fieldset,
    )


class StepFileInline(StackedInline):
    min_num = 0
    max_num = 5
    extra = 0
    model = StepFile


class StepPlugin(BlockPlugin):
    name = 'Step'
    module = 'Steps'
    model = Step
    render_template = 'cms_plugins/steps/step.html'
    inlines = (StepLinkInline, StepFileInline)

    fieldsets = (
        ('Content', {
            'fields': BlockMixin._admin_fields,
        }),
    )


plugin_pool.register_plugin(StepListPlugin)
plugin_pool.register_plugin(StepPlugin)
