from user_profiles.utils import get_user_profile_model
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_profile_model()

class SignupFormBase(forms.Form):
    username = forms.CharField(required=True, max_length=16)
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput)
    password_confirm = forms.CharField(required=True, widget=forms.widgets.PasswordInput)

    class Meta:
        model = User
    
    def clean_username(self):
        existing_user = User.objects.filter(username=self.cleaned_data['username'])
        if existing_user.exists():
            raise forms.ValidationError(_('This username is already taken.'))
        return self.cleaned_data['username']

    def clean_password_confirm(self):
        if 'password' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
            raise forms.ValidationError(_('Password confirmation does not match password.'))
        return self.cleaned_data['password_confirm']
        
    def save(self, commit=True):
        new_user = User(username=self.cleaned_data['username'], 
            email=self.cleaned_data.get('email', ''))
        new_user.set_password(self.cleaned_data.get('password', ''))
        if commit:
            new_user.save()
        return new_user

class SignupForm(SignupFormBase):
    username = forms.EmailField(required=True, max_length=16, label=_('e-Mail address'))
    invitation_code = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput, min_length=6)
    password_confirm = forms.CharField(required=True, widget=forms.widgets.PasswordInput)
    first_name = forms.CharField(max_length=255, required=False) 
    last_name = forms.CharField(max_length=255, required=False) 

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs and 'invitation_code' in kwargs['initial'] and kwargs['initial']['invitation_code']:
            self.fields['invitation_code'].widget = forms.HiddenInput()
        