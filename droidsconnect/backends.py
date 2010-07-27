from google.appengine.ext import db
from google.appengine.api import users
from droidsconnect.account.models import Account
import logging

class GoogleAccountBackend:
    def authenticate(self):
        logging.info("authenticate user")
        user = users.get_current_user()
        q = db.GqlQuery("SELECT * FROM Account where user = :1", user)
        account = q.get()
        if account is None:
            account = Account(user=user)
            account.put()

        return user

