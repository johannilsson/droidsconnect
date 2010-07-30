from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^$', 'droidsconnect.project.views.index'),
    (r'^project/', include('droidsconnect.project.urls')),
    (r'^account/', include('droidsconnect.account.urls')),
    (r'^login/$', 'droidsconnect.auth.views.login'),
    (r'^logout/$', 'droidsconnect.auth.views.logout'),
    (r'^authenticate/$', 'droidsconnect.auth.views.authenticate'),
    (r'^about/$', direct_to_template, {'template': 'about.html'}),
)
