from django import forms
from django_countries.fields import CountryField
from rh.apps.case_studies.models import get_use_cases


class ContactForm(forms.Form):
    name = forms.CharField(label_suffix="*", widget=forms.TextInput(attrs={'placeholder': 'Please enter your full name...'}))
    institution = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Please enter the name of your institution...'}))
    country = CountryField(blank=True).formfield()
    email = forms.EmailField(label_suffix="*", widget=forms.TextInput(attrs={'placeholder': 'Please enter your email address...'}))
    project_scope = forms.ChoiceField(required=False)
    message = forms.CharField(label_suffix="*", widget=forms.Textarea(attrs={'placeholder': 'Any other comments?'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        use_cases = list(get_use_cases())
        use_cases = [('', '--------')] + list(zip(use_cases, use_cases))
        self.fields['project_scope'].choices = use_cases
        self.fields['name'].label = "Full name"
        self.fields['email'].label = "Email address"
        self.label_suffix = ''
