# coding=utf-8

"""
Runserver
"""

__all__ = ['BaseRunserver']

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from source.processes.base import BaseProcess
from app.api.routes import mod_upy


app = Flask(__name__)

def page_not_found(self, error):
    """
    Render 404 error page
    """
    return render_template('404.html'), 404

app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_error_handler(404, page_not_found)
app.register_blueprint(mod_upy)

db = SQLAlchemy(app)
ma = Marshmallow(app)
db.init_app(app)

from app.models.work_process import WorkProcess
from app.models.work_station import WorkStation
from app.models.work_user import WorkUser