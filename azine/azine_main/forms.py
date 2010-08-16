from azine_main.models import Invitation
from django.utils.translation import ugettext_lazy as _
from azine_main.models import Invitation
from django import forms
from django.contrib.auth import forms as auth_forms
from user_profiles import forms as user_profiles_forms
from azine_main import mail
import re

class AuthenticationForm(auth_forms.AuthenticationForm):
    username = forms.CharField(required=True, max_length=30, label=_('e-Mail address'))

class SignupForm(user_profiles_forms.SignupForm):
    username = forms.EmailField(required=True, max_length=30, label=_('e-Mail address'), help_text=_('Your e-Mail address is your username.'))
    invitation_code = forms.CharField(required=True, help_text=_('You need a personal invitation to sign up.'))
    first_name = forms.CharField(max_length=30, required=False) 
    last_name = forms.CharField(max_length=30, required=False) 

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs and 'invitation_code' in kwargs['initial'] and kwargs['initial']['invitation_code']:
            self.fields['invitation_code'].widget = forms.HiddenInput()

    def clean_invitation_code(self):
        invitation = Invitation.objects.filter(invitation_code=self.cleaned_data['invitation_code'])
        if not invitation.exists():
            raise forms.ValidationError(_('This invitation code is not valid.'))
        elif not invitation.filter(created_user=None).exists():
            raise forms.ValidationError(_('This invitation code has already been used.'))
        return self.cleaned_data['invitation_code']

    def save(self, *args, **kwargs):
        user = super(SignupForm, self).save(*args, **kwargs)
        if user:
            invitation = Invitation.objects.get(invitation_code=self.cleaned_data['invitation_code'])
            invitation.created_user = user
            invitation.save()
        return user

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
            invitation.from_user = from_user
            invitation.save()
            mail.sendmail('Invitation', [email])

 