from cms.models import CMSPlugin
from cms.models.fields import PageField
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


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


# ------------------------------------------------------------------------------
# CMS Plugin/Admin
# ------------------------------------------------------------------------------
class StepListPlugin(CMSPluginBase):
    name = 'Step List'
    module = 'Steps'
    model = StepList
    render_template = 'cms_plugins/steps/step_list.html'


plugin_pool.register_plugin(StepListPlugin)
