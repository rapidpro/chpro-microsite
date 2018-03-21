import tagulous

from django.contrib import admin
from django.http import HttpResponseRedirect

from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models import CaseStudy


class CaseStudyAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    change_form_template ='admin/case_study_change_form.html'

    def response_post_save_add(self, request, obj):
        """
        Figure out where to redirect after the 'Save' button has been pressed
        when adding a new object.
        """
        if '_cms_change' in request.POST:
            return HttpResponseRedirect(obj.get_cms_change_url())
        return super().response_post_save_add(request, obj)

    def response_post_save_change(self, request, obj):
        """
        Figure out where to redirect after the 'Save' button has been pressed
        when editing an existing object.
        """
        if '_cms_change' in request.POST:
            return HttpResponseRedirect(obj.get_cms_change_url())
        return super().response_post_save_add(request, obj)


tagulous.admin.register(CaseStudy, CaseStudyAdmin)