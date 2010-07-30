from google.appengine.ext import db

class Account(db.Model):
    user = db.UserProperty()
    nickname = db.StringProperty()
    homepage = db.LinkProperty()
    email = db.EmailProperty()
