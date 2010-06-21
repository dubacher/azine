from azine_main.models import Application
from django import forms
from django.template import Template
from django.shortcuts import render_to_response, get_object_or_404 
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
    pass

@login_required
def add(request, job_id):
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = get_object_or_404(Job, pk=job_id)
            application.applicant = request.user
            application.save()
            send_mail('New Application', 'New Application added.', 'from@azine.me', ['to@test-user.com'], fail_silently=False)
            url = reverse('job_index')
            return HttpResponseRedirect(url)
            
    else:
        form = ApplicationForm()
        
    context_dict = {
        'form': form
    }
                             
    return render_to_response('html/azine_main/application/add.html', 
        context_dict, context_instance=RequestContext(request))
    
@login_required
def index_for_user(request):
    context_dict = {
        'applications': Application.objects.filter(applicant=request.user.id)
    }
    return render_to_response('html/azine_main/application/index.html', 
        context_dict, context_instance=RequestContext(request))