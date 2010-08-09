from user_profiles import settings as app_settings
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.template import Template
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404 
from django.core.exceptions import PermissionDenied
from django.contrib import messages

SIGNUP_SUCCESS_URL = None

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        signup_form = app_settings.SIGNUP_FORM(request.POST)
        if signup_form.is_valid():
            new_user = signup_form.save()
            user_profile_form = app_settings.PROFILE_FORM(request.POST, instance=new_user.get_profile())
            try:
                user_profile_form.save()
                messages.success(request, _('Signup was successful. You can now log in.'))
                return HttpResponseRedirect(SIGNUP_SUCCESS_URL or reverse('login'))
            except Exception as e:
                # This should never happen. However, in case it ever should, delete unusable User:
                new_user.delete()
                raise e
    else:
        signup_form = app_settings.SIGNUP_FORM(initial=request.GET)
    context_dict = {
        'form': signup_form
    }
    return render_to_response('user_profiles/signup.html', 
        context_dict, context_instance=RequestContext(request))

@login_required
def detail(request, username):
    user = get_object_or_404(User, username=username)
    context_dict = {
        'user' : user
    }
    return render_to_response('user_profiles/profile/detail.html',
        context_dict, context_instance=RequestContext(request))

@login_required
def change(request, username):
    if username != request.user.username:
        raise PermissionDenied
    if request.method == 'POST':
        try:
            profile = request.user.get_profile()
            form = app_settings.PROFILE_FORM(request.POST, instance=profile)
        except:
            form = app_settings.PROFILE_FORM(request.POST)        
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, _('Your changes were saved.'))
            return HttpResponseRedirect(reverse('user_detail', args=[request.user.username,]))
    else:
        try:
            profile = request.user.get_profile()
            form = app_settings.PROFILE_FORM(instance=profile)
        except:
            form = app_settings.PROFILE_FORM()
    
    context_dict = {
        'form' : form
    }
    
    return render_to_response('user_profiles/profile/change.html',
        context_dict, context_instance=RequestContext(request))
