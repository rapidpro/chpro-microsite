from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CaseStudyListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w\-]+)/$', views.CaseStudyView.as_view(), name='detail'),
]
