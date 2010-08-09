from django.utils.translation import ugettext as _
from azine_main.forms import InvitationForm
from django.shortcuts import render_to_response, get_object_or_404 
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def add(request):
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            form.save(from_user=request.user)
            messages.add_message(request, messages.SUCCESS, _('Your invitations have been sent'))
            return HttpResponseRedirect('/')
    else:
        form = InvitationForm()
        
    context_dict = {
        'form': form
    }

    return render_to_response('html/azine_main/invitation/add.html', 
        context_dict, context_instance=RequestContext(request))
