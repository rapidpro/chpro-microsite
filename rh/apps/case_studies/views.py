from django.views.generic import DetailView, ListView

from rh.apps.case_studies.models import CaseStudy


class CaseStudyView(DetailView):
    template_name = 'case_studies/case_study.html'
    model = CaseStudy

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(published=True)

        return queryset


class CaseStudyListView(ListView):
    template_name = 'case_studies/case_study_list.html'
    model = CaseStudy

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(published=True)

        return queryset
