form functools import wraps

def a_new_decorator(a_func):
    @waps(a_func)
    def wrapTheFunction():
        print("before a_func()")
        a_func()


