from django.utils.translation import ugettext_lazy as _
from azine_main.models import Invitation
from django import forms
from user_profiles import forms as user_profiles_forms
import re

class SignupForm(user_profiles_forms.SignupForm):
    username = forms.CharField(required=True, max_length=16, label=_('e-Mail address'))
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput)
    password_confirm = forms.CharField(required=True, widget=forms.widgets.PasswordInput)
    first_name = forms.CharField(max_length=255, required=False) 
    last_name = forms.CharField(max_length=255, required=False) 
    
class InvitationForm(forms.ModelForm):
    to_emails = forms.CharField(required=True)

    class Meta:
        model = Invitation

    def __init__(self, *args, **kwargs):
        super(InvitationForm, self).__init__(*args, **kwargs)
        del self.fields['to_email']

    def split_to_emails(self):
        return re.split('\s*,\s*', self.cleaned_data['to_emails'])
        
    def clean_to_emails(self):
        email_addresses = self.split_to_emails()
        # TODO validate all addresses
        return self.cleaned_data['to_emails']        
        
    def save(self, from_user):
        email_addresses = self.split_to_emails()
        invitation_data = self.cleaned_data
        del invitation_data['to_emails']
        for email in email_addresses:
            invitation_data['to_email'] = email
            invitation = Invitation(**invitation_data)
            # TODO if send email:
            invitation.from_user = from_user
            invitation.save()