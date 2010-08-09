from django.conf import settings
from user_profiles.forms import SignupForm, ProfileForm

SIGNUP_FORM = getattr(settings, 'USER_PROFILES_SIGNUP_FORM', SignupForm)
PROFILE_FORM = getattr(settings, 'USER_PROFILES_PROFILE_FORM', ProfileForm)