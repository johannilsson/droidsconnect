from google.appengine.ext import db
from droidsconnect.account.models import Account

class Project(db.Model):
    #owner = db.UserProperty()
    owner = db.ReferenceProperty(Account)
    created_at = db.DateTimeProperty(auto_now_add=True)
    title = db.StringProperty(required=True)
    description = db.TextProperty(required=True)
    type = db.StringProperty(required=True, choices=set(["App", "Game"]))

    developer_description = db.TextProperty()
    artist_description = db.TextProperty()
    copywriter_description = db.TextProperty()

    vcs_url = db.LinkProperty()
    project_url = db.LinkProperty()
    package_name = db.StringProperty()

    icon = db.BlobProperty()

    def needs_developer(self):
        if self.developer_description:
            return True
        return False

    def needs_artist(self):
        if self.artist_description:
            return True
        return False

    def needs_copywriter(self):
        if self.copywriter_description:
            return True
        return False