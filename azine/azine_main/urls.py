from django.conf.urls.defaults import *
from azine_main.rss import LatestEntriesFeed


urlpatterns = patterns('',
	(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'html/azine_main/login/login.html'}),
	(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^job/add/', 'azine_main.views.job_add', name="job_add"),
    url(r'^job/', 'azine_main.views.job_index', name="job_index"),
    url(r'^job/(\d+)/', 'azine_main.views.job_detail', name='job_detail'),
    url(r'^user/change/', 'azine_main.views.user_profile_change', name='user_profile_change'),
    url(r'^application/add/(\d+)/', 'azine_main.views.application_add', name='application_add'),
    url(r'^application/user/', 'azine_main.views.application_index_for_user', name="application_index_for_user"),
    (r'^rss/latest/jobs/$', LatestEntriesFeed()),

)

