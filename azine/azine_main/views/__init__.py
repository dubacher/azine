from django.shortcuts import render_to_response 
from django.template import RequestContext

def tmp_home(request):
    return render_to_response('html/base.html', 
        {}, context_instance=RequestContext(request))
