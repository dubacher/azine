from azine_main.models import Job
from azine_main.models import UserProfile
from azine_main.models import Application
from azine_main.forms.job import JobForm
from django import forms
from django.template import Template
from django.shortcuts import render_to_response, get_object_or_404 
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def add(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save()
            url = reverse('job_detail', args=[job.pk])
            return HttpResponseRedirect(url)
    else:
        form = JobForm()
        
    context_dict = {
        'form': form
    }
    return render_to_response('html/azine_main/job/add.html', 
        context_dict, context_instance=RequestContext(request))

@login_required
def index(request):
    context_dict = {
        'jobs': Job.objects.all()
    }
    return render_to_response('html/azine_main/job/index.html', 
        context_dict, context_instance=RequestContext(request))

@login_required
def detail(request, job_id):
    context_dict = {
        'job': get_object_or_404(Job, pk=job_id)
    }
    return render_to_response('html/azine_main/job/detail.html', 
        context_dict, context_instance=RequestContext(request))

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
    pass

@login_required
def apply(request, job_id):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = get_object_or_404(Job, pk=job_id)
            application.applicant = request.user
            application.save()
            persistent_messages.add_message(request, persistent_messages.INFO, _('Blah'), subject=_('Your application was added'), email=True)
            url = reverse('job_index')
            return HttpResponseRedirect(url)
    else:
        form = ApplicationForm()

    context_dict = {
        'form': form
    }

    return render_to_response('html/azine_main/application/add.html', 
        context_dict, context_instance=RequestContext(request))
