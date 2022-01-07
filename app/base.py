# coding=utf-8

"""
Module Docstring
"""

__all__ = ['BaseApp']

import environ


class BaseApp(object):
    """BaseApp
    """

    def __init__(self):
        """Constructor 
        """
        self.env = environ.Env()