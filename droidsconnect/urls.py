from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'droidsconnect.project.views.index'),
    (r'^project/', include('droidsconnect.project.urls')),
    (r'^account/', include('droidsconnect.account.urls')),
    (r'^login/$', 'droidsconnect.auth.views.login'),
    (r'^logout/$', 'droidsconnect.auth.views.logout'),
    (r'^authenticate/$', 'droidsconnect.auth.views.authenticate'),
    #(r'^project/$', 'droidsconnect.project.views.index'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
