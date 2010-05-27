from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^job/add/', 'azine_main.views.job_add', name="job_add"),
    url(r'^job/index/', 'azine_main.views.job_index', name="job_index"),
    url(r'^job/detail/(\d+)/', 'azine_main.views.job_detail', name='job_detail'),
)

