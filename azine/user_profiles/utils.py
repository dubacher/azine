from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.models import SiteProfileNotAvailable
from django.db import models

def get_user_profile_model():
    """
    Returns site-specific profile for this user. Raises
    SiteProfileNotAvailable if this site does not allow profiles.
    """
    from django.conf import settings
    if not getattr(settings, 'AUTH_PROFILE_MODULE', False):
        raise SiteProfileNotAvailable('You need to set AUTH_PROFILE_MO'
                                      'DULE in your project settings')
    try:
        app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
    except ValueError:
        raise SiteProfileNotAvailable('app_label and model_name should'
                ' be separated by a dot in the AUTH_PROFILE_MODULE set'
                'ting')

    try:
        model = models.get_model(app_label, model_name)
        if model is None:
            raise SiteProfileNotAvailable('Unable to load the profile '
                'model, check AUTH_PROFILE_MODULE in your project sett'
                'ings')
        return model
    except (ImportError, ImproperlyConfigured):
        raise SiteProfileNotAvailable
