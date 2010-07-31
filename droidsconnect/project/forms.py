from google.appengine.ext.db import djangoforms
from droidsconnect.project.models import Project

class ProjectForm(djangoforms.ModelForm):
  class Meta:
    model = Project
    exclude = ['owner', 'created_at', 'icon']
