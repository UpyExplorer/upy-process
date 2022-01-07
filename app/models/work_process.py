# coding=utf-8

"""
Model Config
"""

from app import db, ma
from marshmallow import fields, EXCLUDE
from app.models.base import ModelBase


class WorkProcess(ModelBase):

    __tablename__ = 'work_process'

    work_user_id = db.Column(db.Integer, nullable=True)
    work_station_id = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer, nullable=True)

    def __init__(
        self,
        work_user_id,
        work_station_id,
        status=None):

        self.work_user_id = work_user_id
        self.work_station_id = work_station_id
        self.status = status

    def __repr__(self):
        return '<id %r>' % (self.id)

class WorkProcessSchema(ma.Schema):
    work_user_id = fields.Integer()
    work_station_id = fields.Integer()
    status = fields.Integer()

    class Meta:
        unknown = EXCLUDE
        fields = (
            'id',
            'work_user_id',
            'work_station_id',
            'status'
        )

base_schema = WorkProcessSchema()
base_schemas = WorkProcessSchema(many=True)