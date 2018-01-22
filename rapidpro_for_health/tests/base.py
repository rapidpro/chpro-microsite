from cms import api
from django.test import TestCase


class BaseTestCase(TestCase):
    DEFAULT_LANGUAGE = 'en'
    DEFAULT_TEMPLATE = 'base.html'

    def setUp(self):
        super().setUp()
        self.homepage = api.create_page(
            'Homepage',
            self.DEFAULT_TEMPLATE,
            self.DEFAULT_LANGUAGE,
            published=True
        )
