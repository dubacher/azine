from azine_main.models import UserProfile
from django import forms
from django.template import Template
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
    pass

@login_required
def change(request):
    
    if request.method == 'POST':
        try:
            profile = request.user.get_profile()
            form = UserProfileForm(request.POST, instance=profile)
        except:
            form = UserProfileForm(request.POST)        
        if form.is_valid():
            form.save()
            url = reverse('job_index')
            return HttpResponseRedirect(url)
            
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