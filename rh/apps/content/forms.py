from django import forms
from django_countries.fields import CountryField
from rh.apps.case_studies.models import get_use_cases


class ContactForm(forms.Form):
    name = forms.CharField()
    institution = forms.CharField(required=False)
    country = CountryField(blank=True).formfield()
    email = forms.EmailField()
    project_scope = forms.ChoiceField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        use_cases = list(get_use_cases())
        use_cases = [('', '--------')] + list(zip(use_cases, use_cases))
        self.fields['project_scope'].choices = use_cases
