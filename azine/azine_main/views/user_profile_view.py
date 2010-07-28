from azine_main.models import UserProfile
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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
    pass

@login_required
def detail(request, username):
    user = get_object_or_404(User, username=username)
    context_dict = {
        'user' : user
    }
    return render_to_response('html/azine_main/user_profile/detail.html',
        context_dict, context_instance=RequestContext(request))

@login_required
def change(request, username):
    if username != request.user.username:
        raise PermissionDenied
    if request.method == 'POST':
        try:
            profile = request.user.get_profile()
            form = UserProfileForm(request.POST, instance=profile)
        except:
            form = UserProfileForm(request.POST)        
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, _('Your changes were saved.'))
            return HttpResponseRedirect(reverse('user_detail', args=[request.user.username,]))
    else:
        try:
            profile = request.user.get_profile()
            form = UserProfileForm(instance=profile)
        except:
            form = UserProfileForm()
    
    context_dict = {
        'form' : form
    }
    
    return render_to_response('html/azine_main/user_profile/change.html',
        context_dict, context_instance=RequestContext(request))
        