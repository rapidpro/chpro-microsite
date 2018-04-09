from django.db.models import Count, Q
from django.views.generic import DetailView, ListView

from rh.apps.case_studies.models import CaseStudy, get_use_cases
from rh.apps.content.models import IconCard


class CurrentPageMixin:

    def get_context_data(self, **kwargs):
        kwargs['current_page'] = self.request.current_page
        return super().get_context_data(**kwargs)


class CaseStudyView(CurrentPageMixin, DetailView):
    template_name = 'case_studies/case_study.html'
    model = CaseStudy

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(published=True)

        return queryset

    def get_context_data(self, **kwargs):
        kwargs['similar_case_studies'] = self.object.similar()
        return super().get_context_data(**kwargs)


class CaseStudyListView(CurrentPageMixin, ListView):
    template_name = 'case_studies/case_study_list.html'
    model = CaseStudy

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(published=True)
        use_cases = self.request.GET.getlist('filter')
        if use_cases:
            filter = Q()
            for slug in use_cases:
                filter |= Q(use_cases__title_set__slug=slug)
            queryset = queryset.filter(filter)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['use_cases'] = list(get_use_cases(self.request))
        return ctx
