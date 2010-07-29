from django.conf.urls.defaults import *

urlpatterns = patterns('',
   url(r'^login/$', 'droidsconnect.auth.views.login', name='google_login'),
   url(r'^logout/$', 'droidsconnect.auth.views.logout', name='google_logout'),
   url(r'^authenticate/$', 'droidsconnect.auth.views.authenticate', name='google_authenticate'),
)
