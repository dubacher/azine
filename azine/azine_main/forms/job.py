from azine_main.models import Job
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django import forms
from form_utils.forms import BetterModelForm

class JobForm(BetterModelForm):

    attrs = {
        'id': 'job-form'
    }

    class Meta:
        model = Job
        fieldsets = [
            (_('General information'), {
                'fields': ['title', 'description']
            }),
            (_('Required skills'), {
                'fields': ['required_skills']
            }),
        ]

    def clean_description(self):
        raise forms.ValidationError('Blah adasd')
        
    def clean(self):
        cleaned_data = self.cleaned_data
        if 'title' in cleaned_data and 'description' not in cleaned_data:
            #raise forms.ValidationError('Blah');
            self._errors['description'] = self.error_class([_('sdasdd')])
            
        return self.cleaned_data
        