from django.contrib.sitemaps import Sitemap
from cms.sitemaps import CMSSitemap  # noqa: F401
from rh.apps.case_studies.models import CaseStudy


class CaseStudySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return CaseStudy.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.last_modified
