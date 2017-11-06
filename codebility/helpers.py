from functools import wraps


def print_out(f):
    """Print function output"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        hr = '-' * 40
        print hr
        print '<<<', args, kwargs
        print '>>>'
        print f(*args, **kwargs)
        print hr
    return wrapper
