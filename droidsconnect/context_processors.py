
def get_user(request):
    """
    Assigns the 'user' value to templates. The user is added to the request via the
    GoogleAuthenticationMiddleware middleware.
    """
    return {'user': request.user}
