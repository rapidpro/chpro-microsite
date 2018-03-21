from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class CaseStudiesApphook(CMSApp):
    app_name = "case_studies"
    name = "Case Studies Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["rh.apps.case_studies.urls"]


apphook_pool.register(CaseStudiesApphook)
