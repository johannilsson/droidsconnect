from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import Context, loader, RequestContext
from google.appengine.api import users
from django.core.urlresolvers import reverse
from google.appengine.ext import db
from droidsconnect.project.models import Project

def index(request):
    user = users.get_current_user()
    if user is None:
        return HttpResponseRedirect(users.create_login_url(
            reverse('droidsconnect.account.views.index')))

    projects = db.Query(Project).filter('owner', request.user).order('-created_at').fetch(100)

    template_values = {
        'project_list': projects,
    }

    return render_to_response('account_index.html', template_values,
                              context_instance=RequestContext(request))
