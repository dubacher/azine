from django.conf.urls.defaults import *
from azine_main.rss import LatestEntriesFeed
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
    
    url(r'^signup/$', 'azine_main.views.signup_view.signup', name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'html/azine_main/login/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^pwd/reset/$', auth_views.password_reset, name='password_reset', kwargs={'template_name': 'html/registration/password_reset_form.html'}),
    url(r'^pwd/reset/done/$', auth_views.password_reset_done, kwargs={'template_name': 'html/registration/password_reset_done.html'}),
    url(r'^pwd/reset/confirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, kwargs={'template_name': 'html/registration/password_reset_confirm.html'}),
    url(r'^pwd/reset/complete/$', auth_views.password_reset_complete, kwargs={'template_name': 'html/registration/password_reset_complete.html'}),
    url(r'^pwd/change/$', auth_views.password_change, name='password_change', kwargs={'template_name': 'html/registration/password_change_form.html'}),
    url(r'^pwd/change/done/$', auth_views.password_change_done, kwargs={'template_name': 'html/registration/password_change_done.html'}),
    url(r'^job/(\d+)/apply/$', 'azine_main.views.job_view.apply', name='job_apply'), 
    url(r'^job/(\d+)/$', 'azine_main.views.job_view.detail', name='job_detail'), 
    url(r'^job/add/$', 'azine_main.views.job_view.add', name='job_add'),
    url(r'^job/$', 'azine_main.views.job_view.index', name='job_index'),
    url(r'^profile/(.*?)/change/$', 'azine_main.views.user_profile_view.change', name='user_profile_change'),
    url(r'^profile/(.*?)/applications/$', 'azine_main.views.application_view.index_for_user', name='application_index_for_user'),
    url(r'^profile/(.*?)/$', 'azine_main.views.user_profile_view.detail', name='user_detail'),
    url(r'^rss/latest/jobs/$', LatestEntriesFeed()),

)

