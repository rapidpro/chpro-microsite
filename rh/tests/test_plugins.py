import os

from .base import BaseTestCase

from filer.models import Image
from djangocms_testing.integrity import CMSPluginIntegrity


class DSMPluginIntegrityTestCase(BaseTestCase, CMSPluginIntegrity):

    plugin_exclude_list = [
    ]

    def setUp(self):
        self.homepage = self.create_page('Homepage')

        #photo_path = os.path.join(os.path.dirname(__file__), 'files', 'home-banner.jpg')
        #self.test_image = Image.objects.create(file=photo_path)

        self.plugin_list = [
            ('TextPlugin', {}),
            ('ComplexHeroPlugin', {}),
            ('SectionPlugin', {}),
            ('CardGridPlugin', {}),
            ('CardPlugin', {}),
            ('ImageCardPlugin', {}),
            ('FeaturedAccordionPlugin', {}),
            ('AccordionCardPlugin', {}),
            ('RawHTMLPlugin', {}),
            ('BlockQuotePlugin', {}),
            ('PaginationPlugin', {}),
            ('StepListPlugin', {'root': self.homepage}),
            ('StepPlugin', {}),
        ]

