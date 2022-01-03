# coding=utf-8

"""
Runserver
"""

__all__ = ['BaseRunserver']

from waitress import serve
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.api.routes import mod_upy

from source.processes.base import BaseProcess


class BaseRunserver(object):
    """
    Class that initializes the project
    """

    def __init__(self):
        """
        Constructor
        """
        app = Flask(__name__)

        self.initialize_app(app)
        self.process()

        host = app.config['HOST']
        port = app.config['PORT']

        # app.run(host=host, port=port)
        serve(app, host=host, port=port)

    def initialize_app(self, app):
        """
        Application preparation before start
        """
        app.config.from_object('config')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        app.register_error_handler(404, self.page_not_found)
        app.register_blueprint(mod_upy)

        db = SQLAlchemy(app)
        db.init_app(app)

    def process(self):
        """
        """
        new_process = BaseProcess()
        new_process.run(key='task_queue')

    def page_not_found(self, error):
        """
        Render 404 error page
        """
        return render_template('404.html'), 404
