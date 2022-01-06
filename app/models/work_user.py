# coding=utf-8

"""
Model Config
"""

from app import db, ma
from marshmallow import fields, EXCLUDE
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)

class WorkUser(Base):

    __tablename__ = 'work_user'

    key = db.Column(db.Integer, nullable=True)
    user_name = db.Column(db.String(50), nullable=True)
    status = db.Column(db.Integer, nullable=True)

    def __init__(
        self,
        key,
        user_name=None,
        status=None):

        self.key = key
        self.user_name = user_name
        self.status = status

    def __repr__(self):
        return '<id %r>' % (self.id)

class WorkUserSchema(ma.Schema):
    key = fields.Str()
    user_name = fields.Str()
    status = fields.Integer()

    class Meta:
        unknown = EXCLUDE
        fields = (
            'id',
            'key',
            'user_name',
            'status'
        )

base_schema = WorkUserSchema()
base_schemas = WorkUserSchema(many=True)