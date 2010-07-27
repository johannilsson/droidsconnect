from django import shortcuts
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context, loader, RequestContext
from google.appengine.api import users
from django.core.urlresolvers import reverse
import logging
from google.appengine.ext import db

def index(request):
    user = users.get_current_user()
    if user is None:
        return HttpResponseRedirect(users.create_login_url(
            reverse('droidsconnect.account.views.index')))

    q = db.GqlQuery("SELECT * FROM Project WHERE owner = :1", user)
    projects = q.fetch(20)
    template_values = {
        'project_list': projects,
    }

    return shortcuts.render_to_response('account_index.html', template_values,
                           context_instance=RequestContext(request))

