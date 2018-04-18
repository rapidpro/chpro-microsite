import json
import logging
from textwrap import dedent

from django import shortcuts
from django.http import HttpResponseBadRequest
from django.core.mail import mail_managers

from . import forms

logger = logging.getLogger(__name__)


def contact_form(request):
    form = forms.ContactForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        message = dedent(f'''
            Name:          {data['name']}
            Institution:   {data['institution']}
            Email:         {data['email']}
            Country:       {data['country']}
            Project Scope: {data['project_scope']}

            Message:
            {data['message']}
        ''')
        mail_managers('Contact', message=message)
        return shortcuts.redirect('/thank-you/')
    logger.info('Invalid contact form submission received: {}'.format(
        json.dumps(form.errors, indent=2)))
    if request.is_ajax():
        # If it's an ajax request we can send back some helpful messages.
        return HttpResponseBadRequest(json.dumps(form.errors))
    # Otherwise just send the user back where they came from.
    referer = request.META.get('HTTP_REFERER') or '/'
    return shortcuts.redirect(referer)
