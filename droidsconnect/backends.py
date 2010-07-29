from google.appengine.ext import db
from google.appengine.api import users
from droidsconnect.account.models import Account
import logging

class GoogleAccountBackend:
    def authenticate(self):
        """
        Called when a user is authenticated. If a Account does not exists
        one will be created.
        """
        logging.info("authenticate user")
        user = users.get_current_user()
        q = db.GqlQuery("SELECT * FROM Account where user = :1", user)
        account = q.get()
        if account is None:
            account = Account(user=user)
            account.nickname = user.nickname()
            if user.email():
                account.email = user.email()
            account.put()

        return account
