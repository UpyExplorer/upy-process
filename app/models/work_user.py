# coding=utf-8

"""
Model Config
"""

from app import db, ma
from marshmallow import fields, EXCLUDE
from app.models.base import ModelBase


class WorkUser(ModelBase):

    __tablename__ = 'work_user'

    company_data_id = db.Column(db.Integer, nullable=True)
    corporate_name = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer, nullable=True)

    def __init__(
        self,
        company_data_id,
        corporate_name=None,
        status=None):

        self.company_data_id = company_data_id
        self.corporate_name = corporate_name
        self.status = status

    def __repr__(self):
        return '<id %r>' % (self.id)

class WorkUserSchema(ma.Schema):
    company_data_id = fields.Str()
    corporate_name = fields.Str()
    status = fields.Integer()

    class Meta:
        unknown = EXCLUDE
        fields = (
            'id',
            'company_data_id',
            'corporate_name',
            'status'
        )

base_schema = WorkUserSchema()
base_schemas = WorkUserSchema(many=True)