from django.conf.urls.defaults import *
from azine_main.rss import LatestEntriesFeed
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
    
    url(r'^job/(\d+)/apply/$', 'azine_main.views.job_views.apply', name='job_apply'), 
    url(r'^job/(\d+)/$', 'azine_main.views.job_views.detail', name='job_detail'), 
    url(r'^job/add/$', 'azine_main.views.job_views.add', name='job_add'),
    url(r'^job/$', 'azine_main.views.job_views.index', name='job_index'),
    url(r'^profile/you/applications/$', 'azine_main.views.application_views.index_for_current_user', name='application_index_for_current_user'),
    url(r'^rss/latest/jobs/$', LatestEntriesFeed()),
    url(r'^invitation/add/$', 'azine_main.views.invitation_views.add', name='invitation_add'),

)

