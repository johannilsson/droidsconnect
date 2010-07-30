from google.appengine.api import users
from google.appengine.ext import db
from droidsconnect.account.models import Account

class GoogleAuthenticationMiddleware(object):
    def process_request(self, request):
        """
        Adds the authenticated account as 'user' to the request.
        """
        user = users.get_current_user()
        if user:
            request.user = db.Query(Account).filter('user', user).get()
        else:
            request.user = None
        return None