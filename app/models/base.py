# coding=utf-8

"""
Model Base
"""

from app import db


class ModelBase(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
