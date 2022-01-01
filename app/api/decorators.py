# coding=utf-8

from flask import request
from functools import wraps


class BaseDecorator(object):
    """ 
    Base View to Decorators common to all Webservices.
    """

    def __init__(self):
        """Constructor
        """
        pass

    def system(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            body = request.data.decode("UTF-8")
            params = request.args.to_dict(flat=False)

            data = {
                "body": body,
                "params": params
            }

            return f(data, *args, **kwargs)
        
        return decorated