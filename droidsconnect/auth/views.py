from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate as django_authenticate, REDIRECT_FIELD_NAME
from google.appengine.api import users

def login(request):
    return HttpResponseRedirect(users.create_login_url(
        reverse('droidsconnect.auth.views.authenticate')
    ))

def logout(request):
    return HttpResponseRedirect(users.create_logout_url("/"))

def authenticate(request):
    user = django_authenticate()
    if user is not None:
        return HttpResponseRedirect('/')
    else:
        # return invalid login page
        return HttpResponseRedirect('/invalid')
