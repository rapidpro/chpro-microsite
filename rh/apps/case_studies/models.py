import random
from django.urls import reverse
from django.db import models

from cms.models import PlaceholderField, Title, Page
from filer.fields.image import FilerImageField
from django_countries.fields import CountryField

from autoslug import AutoSlugField


def get_use_cases(request=None):
    """
    Get all use cases.

    Return an iterable of pages that are found in the first
    CardGridPlugin on the page with the slug "use-cases".
    """
    try:
        obj = Title.objects.public().get(slug='use-cases').page
    except Title.DoesNotExist:
        return
    if request:
        filters = request.GET.getlist('filter')
    for child in obj.get_children():
        if request:
            slug = child.get_slug()
            iconf = filters[:]
            child.selected = slug in iconf
            if child.selected:
                iconf.remove(slug)
                request.use_cases_filtered = True
            else:
                iconf.append(slug)
            qd = request.GET.copy()
            qd.setlist('filter', iconf)
            child.url = qd.urlencode()
        yield child


def use_case_choices():
    return {'pk__in': [case.pk for case in get_use_cases()]}


class CaseStudy(models.Model):
    REGIONS = (
        ('americas', 'The Americas and Caribbean'),
        ('europe-asia-c', 'Europe and Central Asia'),
        ('pacific-asia-e', 'East Asia and the Pacific'),
        ('africa-e-s', 'Eastern and Southern Africa'),
        ('middle-east-africa', 'Middle East and North Africa'),
        ('asia-s', 'South Asia'),
        ('africa-w-c', 'West and Central Africa'),
    )
    region = models.CharField(max_length=20, choices=REGIONS)
    countries = CountryField(multiple=True)
    heading = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='heading', unique=True, max_length=128)
    featured_image = FilerImageField(verbose_name='Featured Image', blank=True,
                                     null=True, related_name='+', on_delete=models.SET_NULL)

    lead_content = PlaceholderField(slotname='case_study_lead_content',
                                    related_name='lead_case_study',
                                    verbose_name='Case Study Lead Content')
    main_content = PlaceholderField(slotname='case_study_main_content',
                                    related_name='main_case_study',
                                    verbose_name='Case Study Main Content')
    stats_content = PlaceholderField(slotname='case_study_stats_content',
                                     related_name='stats_case_study',
                                     verbose_name='Case Study Stats Content')
    sidebar_content = PlaceholderField(slotname='case_study_sidebar_content',
                                       related_name='sidebar_case_study',
                                       verbose_name='Case Study Sidebar Content')

    published = models.BooleanField('Published', default=False,
        help_text='Indicates if this Case Study is pubilc or still a draft.')

    last_modified = models.DateTimeField(auto_now=True)

    use_cases = models.ManyToManyField(
        Page, limit_choices_to=use_case_choices)

    class Meta:
        verbose_name_plural = 'Case Studies'

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        """
        Absolute URL for this object. Expects a given Application name
        to reverse the URL to the correct location.
        """

        return reverse('case_studies:detail', kwargs={'slug': self.slug})

    def get_cms_change_url(self):
        return '{}?edit'.format(self.get_absolute_url())

    def similar(self, count=4, only_published=True):
        qs = CaseStudy.objects.exclude(pk=self.pk)
        if only_published:
            qs = qs.filter(published=True)
        qs = qs
        similar_cases = list(
            qs.filter(use_cases__in=self.use_cases.all()).order_by()
            .distinct())
        if len(similar_cases) > count:
            similar_cases = random.sample(similar_cases, count)
        else:
            random.shuffle(similar_cases)
        print(similar_cases)
        remaining = count - len(similar_cases)
        if remaining > 0:
            similar_cases.extend(list(
                qs.exclude(pk__in=[case.pk for case in similar_cases])
                .order_by('?')[:remaining]))
        return similar_cases
