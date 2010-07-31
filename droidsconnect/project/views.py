from django import shortcuts
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.api import images
from droidsconnect.project.forms import ProjectForm
from droidsconnect.project.models import Project
import logging
import markdown
import django.http

def index(request):
    #q = db.GqlQuery("SELECT * FROM Project")
    #projects = q.fetch(20)
    projects = db.Query(Project).order('-created_at').fetch(100)
    template_values = {
        'project_list': projects,
    }

    return shortcuts.render_to_response('index.html', template_values,
                           context_instance=RequestContext(request))

def create(request):
    # TODO: create a decorator: @requires_login(users.create_login_url...)
    user = users.get_current_user()
    if user is None:
        return HttpResponseRedirect(users.create_login_url(
            reverse('droidsconnect.project.views.create')))

    if request.method == 'POST':
        #form = ProjectForm(request.POST)
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            try:
                project = form.save(commit=False)
                project.owner = request.user
            except ValueError, err:
                # TODO: Handle errors...
                pass
            else:
                project.put()

            if request.FILES:
                uploaded_icon = request.FILES['icon']
                # TODO: Check for exceptions here...
                icon = images.resize(uploaded_icon['content'], 72, 72)
                project.icon = db.Blob(icon)

            project.put()

            key = project.key()
            id = str(key)

            return HttpResponseRedirect(
                reverse('droidsconnect.project.views.detail', args=[id]))
        else:
            logging.info("not valid...")

    else:
        form = ProjectForm()

    template_values = {
        'form': form,
    }

    return shortcuts.render_to_response('project_create.html', template_values,
                           context_instance=RequestContext(request))

def edit(request, project_id):
    user = users.get_current_user()
    if user is None:
        return HttpResponseRedirect(users.create_login_url('/'))
    try:
        key = db.Key(encoded=project_id)
        project = db.Query(Project).filter('owner', request.user).filter('__key__', key).get()
    except:
        raise Http404
    else:
        if project is None:
            raise Http404

    form = ProjectForm(data=request.POST or None, instance=project)
    if request.method == 'POST':
        if form.is_valid():
            try:
                project = form.save(commit=False)
            except ValueError, err:
                pass

            if request.FILES:
                uploaded_icon = request.FILES['icon']
                # TODO: Check for exceptions here...
                icon = images.resize(uploaded_icon['content'], 72, 72)
                project.icon = db.Blob(icon)

            project.put()

    template_values = {
        'form': form,
        'project': project,
    }

    return shortcuts.render_to_response('project_edit.html', template_values,
                           context_instance=RequestContext(request))

def detail(request, project_id):
    # TODO: add result to memcache...
    # event = Event.get_by_id(long(event_id)
    try:
        key = db.Key(encoded=project_id)
        q = db.GqlQuery("SELECT * FROM Project " +
                    "WHERE __key__ = :1", key)
        project = q.get()
    except:
        raise Http404

    md = markdown.Markdown()
    description = md.convert(project.description)
    template_values = {
        'project': project,
        'description': description,
    }

    return shortcuts.render_to_response('project_detail.html', template_values,
                           context_instance=RequestContext(request))

def icon(request, project_id):
    try:
        key = db.Key(encoded=project_id)
        q = db.GqlQuery("SELECT * FROM Project " +
                    "WHERE __key__ = :1", key)
        project = q.get()
    except:
        raise Http404

    if project.icon:
        response = HttpResponse(project.icon, mimetype='image/png')
    else:
        raise Http404

    return response
