from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'html/azine_main/login/login.html'}),
	(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^job/add/', 'azine_main.views.job_add', name="job_add"),
    url(r'^job/index/', 'azine_main.views.job_index', name="job_index"),
    url(r'^job/detail/(\d+)/', 'azine_main.views.job_detail', name='job_detail'),
    url(r'^user/update/', 'azine_main.views.user_profile_update', name='user_profile_update'),
)

