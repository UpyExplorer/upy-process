# coding=utf-8

"""
Model Config
"""

from app import db, ma
from marshmallow import fields, EXCLUDE
from app.models.base import ModelBase


class WorkProcess(ModelBase):

    __tablename__ = 'work_process'

    work_user = db.Column(db.Integer, db.ForeignKey('work_user.id'), nullable=False)
    work_station = db.Column(db.Integer, db.ForeignKey('work_station.id'), nullable=False)
    status = db.Column(db.Integer, nullable=True)

    def __init__(
        self,
        work_user,
        work_station,
        status=None):

        self.work_user = work_user
        self.work_station = work_station
        self.status = status

    def __repr__(self):
        return '<id %r>' % (self.id)

class WorkProcessSchema(ma.Schema):
    work_user = fields.Str()
    work_station = fields.Str()
    status = fields.Integer()

    class Meta:
        unknown = EXCLUDE
        fields = (
            'id',
            'work_user',
            'work_station',
            'status'
        )

base_schema = WorkProcessSchema()
base_schemas = WorkProcessSchema(many=True)