from django.conf.urls.defaults import *

urlpatterns = patterns('droidsconnect.project.views',
    (r'^create/$', 'create'),
    (r'^(?P<project_id>[0-9A-Za-z]+)/edit/$', 'edit'),
    (r'^(?P<project_id>[0-9A-Za-z]+)/$', 'detail'),
    (r'^(?P<project_id>[0-9A-Za-z]+)/icon/$', 'icon'),
    #(r'^(?P<project_id>[0-9A-Za-z]+)/icon/create/$', 'icon_create'),
    (r'^(?P<project_id>[0-9A-Za-z]+)/contact/$', 'contact'),
)
