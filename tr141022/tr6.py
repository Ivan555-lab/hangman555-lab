from functools import wraps

def requires_auth(f):
    @wrap(f)
    def decrated(*args, **kwargs):
        auth = request.authorization
