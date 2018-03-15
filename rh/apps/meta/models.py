from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


# ------------------------------------------------------------------------------
# Models
# ------------------------------------------------------------------------------


class MetaAttributes(PageExtension):
    description = HTMLField(blank=True, null=True)
    icon = FilerImageField(blank=True, null=True)

extension_pool.register(MetaAttributes)



from django.contrib import admin
from cms.extensions import PageExtensionAdmin


class IconExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(MetaAttributes, IconExtensionAdmin)


from cms.admin.pageadmin import PageAdmin
from cms.models.pagemodel import Page
from django.contrib import admin


class PageAvatarsAdmin(admin.TabularInline):
    model = MetaAttributes


PageAdmin.inlines.append(PageAvatarsAdmin)

admin.site.unregister(Page)
admin.site.register(Page, PageAdmin)


# ------------------------------------------------------------------------------
# CMS Plugin/Admin
# ------------------------------------------------------------------------------
# class MetaAttributesPlugin(CMSPluginBase):
#     name = 'Meta Attributes'
#     module = 'Meta'
#     model = MetaAttributes
#     render_template = "cms_plugins/meta/empty.html"
#
#     fieldsets = (
#         ('Listing', {
#             'fields': ('icon', 'description')
#         }),
#     )
#
#
# plugin_pool.register_plugin(MetaAttributesPlugin)
