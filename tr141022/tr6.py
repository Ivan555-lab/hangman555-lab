from functools import wraps

def requires_auth(f):
    @wrap(f)
    def decrated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated
