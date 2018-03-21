from django.contrib import admin

from .models import CustomSVGIcon


class CustomSVGIconAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview')

    def preview(self, obj):
        return '<img style="width: 100px; height: 40px;" src="{}"/>'.format(obj.svg.url)
    preview.allow_tags = True


admin.site.register(CustomSVGIcon, CustomSVGIconAdmin)
