# coding=utf-8

"""
Runserver
"""

__all__ = ['BaseRunserver']

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.api.routes import mod_upy

from source.processes.base import BaseProcess

app = Flask(__name__)

class BaseRunserver(object):
    """
    Class that initializes the project
    """

    def __init__(self):
        """
        Constructor
        """
        self.initialize_app(app)
        self.run()

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

    def run(self):
        """
        """
        app.run(host=app.config['HOST'],port=app.config['PORT'])
        self.process()

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
