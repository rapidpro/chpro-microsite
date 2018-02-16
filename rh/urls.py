from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
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
