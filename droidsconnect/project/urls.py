from django.conf.urls.defaults import *

urlpatterns = patterns('droidsconnect.project.views',
    (r'^create/$', 'create'),
    (r'^(?P<project_id>[0-9A-Za-z]+)/$', 'detail'),
)
