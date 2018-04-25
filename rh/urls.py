from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.defaults import page_not_found
from rh.apps.content.views import contact_form
from . import sitemaps
from .views import server_error

urlpatterns = [
    url(r'^404/$', page_not_found, kwargs={'exception': ''}),
    url(r'^500/$', server_error),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {
        'cmspages': sitemaps.CMSSitemap,
        'case-studies': sitemaps.CaseStudySitemap,
    }}),
    url(r'^send_contact_form/', contact_form, name='contact_form'),
    url(r'^admin/', admin.site.urls),
    url(r'^select2/', include('django_select2.urls')),

    # Django CMS
    url(r'^', include('cms.urls')),
]

if settings.DEBUG:  # pragma: no cover
    try:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        print('DEBUG is set to True, and debug_toolbar is not installed. Skipping.')

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom 500 error view.
handler500 = server_error
