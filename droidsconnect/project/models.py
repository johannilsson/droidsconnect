from google.appengine.ext import db
from droidsconnect.account.models import Account

class Project(db.Model):
    owner = db.UserProperty()
    #owner = db.ReferenceProperty(Account)
    created_at = db.DateTimeProperty(auto_now_add=True)
    title = db.StringProperty(required=True)
    description = db.TextProperty(required=True)
    type = db.StringProperty(required=True, choices=set(["App", "Game"]))
    
    needs_developer = db.BooleanProperty()
    needs_developer_list = db.TextProperty()
    
    needs_artist = db.BooleanProperty()
    needs_artist_list = db.TextProperty()
    
    needs_copywriter = db.BooleanProperty()
    needs_artist_list = db.TextProperty()
    
    vcs_url = db.LinkProperty()
    project_url = db.LinkProperty()
    package_name = db.StringProperty()
    