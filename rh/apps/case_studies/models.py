from django.urls import reverse
from django.db import models

from cms.models import PlaceholderField
from filer.fields.image import FilerImageField

from django_countries.fields import CountryField
from tagulous.models import TagField
from autoslug import AutoSlugField


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

    tags = TagField(verbose_name='Tags', blank=True)

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

