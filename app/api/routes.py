# coding=utf-8

"""
Module Docstring
"""

from flask import Blueprint, redirect
from app.api.decorators import BaseDecorator

mod_upy = Blueprint('', __name__, url_prefix='')


class UpyView(object):
    """Base View
    """
    def __init__(self):
        super().__init__()

    @mod_upy.route('/', methods=['GET'])
    @BaseDecorator.system
    def initial(data):
        return redirect("http://upyexplorer.com/")
