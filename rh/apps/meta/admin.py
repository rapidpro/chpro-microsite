from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import MetaAttributes


class MetaAttributesAdmin(PageExtensionAdmin):
    exclude = ['plugins']

admin.site.register(MetaAttributes, MetaAttributesAdmin)