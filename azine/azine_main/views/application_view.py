from azine_main.models import Application
from azine_main.decorators import private_user_page
from django.contrib.auth.models import User
from django import forms
from django.template import Template
from django.shortcuts import render_to_response, get_object_or_404 
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# TODO!
@private_user_page
def index_for_user(request, username):
    user = get_object_or_404(User, username=username)
    context_dict = {
        'applications': Application.objects.filter(applicant=user)
    }
    return render_to_response('html/azine_main/application/index.html', 
        context_dict, context_instance=RequestContext(request))