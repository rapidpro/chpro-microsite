from __future__ import unicode_literals

import operator
from os import path
from glob import glob
from logging import getLogger

from django.db.models.fields import CharField
from django.db.utils import DatabaseError, ProgrammingError
from django.conf import settings
from django.utils import six
from django import forms

logger = getLogger(__file__)


# Full path to the icons folder (<project>/client/static/icons/)
ICONS_FOLDER = path.join(settings.PROJECT_DIR, 'client', 'static', 'icons')


def get_icon_choices():
    """
    Reads the SVG ``client/static/icons/`` static file folder and returns all icons
    with their filename and a title.

    :return: Choices of icons with their [file]name and title.
    """
    def title(s):
        """
        Create a better title of a given filename. Function will capitalize
        all found words (words separated by dashes) and also rename some known
        artifacts. Example::

            'speech-bubbles.svg' becomes 'Speech Bubbles'
            'usa-map.svg' becomes 'USA Map'

        :param filename: icon filename
        :return: (string) Title of the icon
        """
        # Replace words (after they got capitalized)
        words = {'Usa': 'USA'}

        s = path.basename(s)
        s = s.replace('.svg', '')                               # Remove trailing .svg
        s = ' '.join([i.capitalize() for i in s.split('-')])    # Capitalize words
        for w, r in six.iteritems(words):
            s = s.replace(w, r)                                 # Replace known words
        return s

    choices = []

    # Sprite Icons from the icons folder
    for icon in glob(ICONS_FOLDER + '/*.svg'):
        choices.append((path.basename(icon).replace('.svg', ''), title(icon)))

    # Custom uploaded icons
    try:
        from .models import CustomSVGIcon
        for icon in CustomSVGIcon.objects.all():
            choices.append((icon.prefixed_id, icon.name))

    # We (can) have a tricky circular condition in migrations here. The
    # IconField is calling this method, which relies on the custom SVG
    # Icon table, which doesn't exist because it's exact migration is
    # running right now.
    except (ProgrammingError, DatabaseError) as e:
        logger.debug("Skipping setup of custom uploaded icons. DB is not ready")

    choices.sort(key=operator.itemgetter(1))
    return choices


class IconChoiceField(forms.ChoiceField):
    """
    Icon Choice field with a list of all choices
    """
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'widget': forms.Select(attrs={'class': 'icon-selector'}),
            'choices': get_icon_choices(),
        })
        super(IconChoiceField, self).__init__(*args, **kwargs)


class IconField(CharField):
    """
    Custom IconField. Pretty much a standard Charfield but defines
    an IconChoiceField that brings all our Icons as choices.
    """
    def formfield(self, **kwargs):
        return IconChoiceField(required=(not getattr(self, 'blank', False)))
