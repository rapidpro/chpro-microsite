from django.urls import reverse
from django.db import models

from cms.models import PlaceholderField, Title
from filer.fields.image import FilerImageField

from django_countries.fields import CountryField
from autoslug import AutoSlugField

from rh.apps.content.models import IconCard


def get_use_cases(request=None):
    """
    Get all use cases.

    Return an iterable of icon cards that are found in the first
    CardGridPlugin on the page with the slug "use-cases".
    """
    page = Title.objects.public().get(slug='use-cases').page
    plugins = page.placeholders.all()[0].get_plugins()
    card_grid = plugins.filter(plugin_type='CardGridPlugin')[0]
    filters = request.GET.getlist('filter') if request else None
    for child in card_grid.get_children():
        iconcard = child.get_plugin_instance()[0]
        if isinstance(iconcard, IconCard):
            if filters is not None:
                iconf = filters[:]
                pk = str(iconcard.pk)
                iconcard.selected = pk in iconf
                iconf.remove(pk) if iconcard.selected else iconf.append(pk)
                qd = request.GET.copy()
                qd.setlist('filter', iconf)
                iconcard.url = qd.urlencode()
            yield iconcard


def use_case_choices():
    return {'pk__in': [case.pk for case in get_use_cases()]}


class CaseStudy(models.Model):
    country = CountryField()
    heading = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='heading', unique=True, max_length=128)
    featured_image = FilerImageField(verbose_name='Featured Image', blank=True,
                                     null=True, related_name='+',  on_delete=models.SET_NULL)

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

    use_cases = models.ManyToManyField(
        IconCard, limit_choices_to=use_case_choices)

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
        qs = qs.filter(use_cases__in=self.use_cases.all())
        return qs.order_by('?')[:count]
