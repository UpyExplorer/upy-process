# coding=utf-8

from flask import Blueprint, jsonify
from app.api.decorators import BaseDecorator

mod_upy = Blueprint('', __name__, url_prefix='')


class UpyView(object):
    """
    Class responsible for Driver Rating information
    """
    def __init__(self):
        super().__init__()

    @mod_upy.route('/', methods=['GET'])
    @BaseDecorator.system
    def get_driver_score(data):
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
