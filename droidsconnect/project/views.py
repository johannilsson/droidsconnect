from django import shortcuts
from django.http import HttpResponseRedirect, Http404
from django.template import Context, loader, RequestContext
from google.appengine.api import users
from django.core.urlresolvers import reverse
from droidsconnect.project.forms import ProjectForm, ProjectModelForm
from droidsconnect.project.models import Project
import logging
from google.appengine.ext import db
import markdown

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
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = Project(title=form.clean_data['title'],
                          type=form.clean_data['type'],
                          description=form.clean_data['description'],
                          owner=request.user)
            project.needs_developer = form.clean_data['needs_developer']
            project.needs_artist = form.clean_data['needs_artist']
            project.needs_copywriter = form.clean_data['needs_copywriter']
            if form.clean_data['vcs_url'] != '':
                project.vcs_url = form.clean_data['vcs_url']
            if form.clean_data['project_url'] != '':
                project.project_url = form.clean_data['project_url']
            if form.clean_data['package_name'] != '':
                project.package_name = form.clean_data['package_name']

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

    form = ProjectModelForm(data=request.POST or None, instance=project)
    if request.method == 'POST':
        if form.is_valid():
            try:
                project = form.save(commit=False)
            except ValueError, err:
                pass
            else:
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
