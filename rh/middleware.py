# -*- coding: utf-8 -*-
from django.utils.functional import SimpleLazyObject
from django.core.urlresolvers import Resolver404, reverse

from cms.utils.compat.dj import MiddlewareMixin
from cms.utils.moderator import use_draft
from cms.models.pagemodel import Page
from cms.utils.i18n import get_language_list
from cms.appresolver import APP_RESOLVERS


# modified     from cms.appresolver import applications_page_check
def applications_page_check(request, current_page=None, path=None):
    """Tries to find if given path was resolved over application.
    Applications have higher priority than other cms pages.
    """
    if current_page:
        return current_page
    if path is None:
        # We should get in this branch only if an apphook is active on /
        # This removes the non-CMS part of the URL.
        path = request.path_info.replace(reverse('pages-root'), '', 1)
        # check if application resolver can resolve this
    for lang in get_language_list():
        if path.startswith(lang + "/"):
            path = path[len(lang + "/"):]
    for resolver in APP_RESOLVERS:
        try:
            page_id = resolver.resolve_page_id(path)
            # yes, it is application page
            page = Page.objects.public().get(id=page_id)
# vvv  added
            if use_draft(request):
                page = page.publisher_public
# ^^^  end added
            # If current page was matched, then we have some override for
            # content from cms, but keep current page. Otherwise return page
            # to which was application assigned.
            return page
        except Resolver404:
            # Raised if the page is not managed by an apphook
            pass
        except Page.DoesNotExist:
            pass
    return None


# modified     from cms.middleware.page import get_page
# vvv  single commented import line
def get_page(request):
    # from cms.appresolver import applications_page_check
    from cms.utils.page_resolver import get_page_from_request

    if not hasattr(request, '_current_page_cache'):
        request._current_page_cache = get_page_from_request(request)
        if not request._current_page_cache:
            # if this is in a apphook
            # find the page the apphook is attached to
            request._current_page_cache = applications_page_check(request)
    return request._current_page_cache


class BetterCurrentPageMiddleware(MiddlewareMixin):
    """
    This custom middleware is required to ensure the correct parent node
    is selected when dealing with apphooks which have cms-editable
    models.
    """
    def process_request(self, request):
        request.current_page = SimpleLazyObject(lambda: get_page(request))
        return None
