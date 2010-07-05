from django.contrib.auth.models import User
from azine_main.models import UserProfile
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
import datetime


class SignupForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email_address = forms.EmailField()


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(request.POST['last_name'], request.POST['email_address'], password=None)
            user_profile = UserProfile(user=new_user, first_name = request.POST['first_name'], last_name = request.POST['last_name'], ip_address = request.get_host(), signup_date = datetime.datetime.now())
            user_profile.save()
            return render_to_response('html/azine_main/signup/signup_successful.html', context_instance=RequestContext(request))            
    else:
        form = SignupForm()
        
    context_dict = {
        'form': form
    }
                             
    return render_to_response('html/azine_main/signup/signup.html', 
        context_dict, context_instance=RequestContext(request))

