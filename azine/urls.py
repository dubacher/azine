from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('azine_main.urls')),

    (r'^googlehostedservice\.html$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'path': 'googlehostedservice.html'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    (r'^messages/', include('persistent_messages.urls')),

    url(r'^user/', include('user_profiles.urls')),
    url(r'^', include('cms.urls')),
)

