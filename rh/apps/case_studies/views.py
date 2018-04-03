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
            for use_case in use_cases:
                if not use_case.isdigit():
                    continue
                filter |= Q(use_cases=use_case)
            queryset = queryset.filter(filter)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = self.get_queryset()
        ctx['tags'] = list(qs.values('tags__name').annotate(Count('id')).values_list('tags__name', flat=True))
        ctx['use_cases'] = list(get_use_cases(self.request))
        return ctx
