from google.appengine.api import users

def get_user(request):
    user = users.get_current_user()
    return {'user': user}
