from django.conf.urls.defaults import *
from azine_main.rss import LatestEntriesFeed
from django.contrib.auth import views

urlpatterns = patterns('',
	(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'html/azine_main/login/login.html'}),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	url(r'^pwd/reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
	url(r'^pwd/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
	url(r'^pwd/reset/confirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm'),
	url(r'^pwd/reset/complete/$', 'django.contrib.auth.views.password_reset_complete'),
	url(r'^pwd/change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^pwd/change/done/$', 'django.contrib.auth.views.password_change_done'),
    url(r'^job/(\d+)/', 'azine_main.views.job_view.detail', name='job_detail'),	
    url(r'^job/add/', 'azine_main.views.job_view.add', name="job_add"),
    url(r'^job/', 'azine_main.views.job_view.index', name="job_index"),
    url(r'^user/change/', 'azine_main.views.user_profile_view.change', name='user_profile_change'),
    url(r'^application/add/(\d+)/', 'azine_main.views.application_view.add', name='application_add'),
    url(r'^application/user/', 'azine_main.views.application_view.index_for_user', name="application_index_for_user"),
    (r'^rss/latest/jobs/$', LatestEntriesFeed()),

)

