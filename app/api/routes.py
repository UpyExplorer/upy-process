# coding=utf-8

from flask import Blueprint, jsonify, redirect
from app.api.decorators import BaseDecorator
from source.processes.base import BaseProcess

mod_upy = Blueprint('', __name__, url_prefix='')


class UpyView(object):
    """
    Class responsible for Driver Rating information
    """
    def __init__(self):
        super().__init__()

    @mod_upy.route('/', methods=['GET'])
    @BaseDecorator.system
    def initial(data):
        return redirect("http://upyexplorer.com/")
        return jsonify(
                {
                    "data": {
                        "status": "success",
                        "message": "Successful Request",
                        "limit": 1,
                        "total": 1
                    },
                    "result": None
                }
            ), 200
