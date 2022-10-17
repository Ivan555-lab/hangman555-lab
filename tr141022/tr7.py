from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was executed")
        return func(*args, **kwargs)
    return with_logging()

@logit
def addition_func(x):
    """Count """
    return x + x

result = addition_func(4)
# new_f 5
