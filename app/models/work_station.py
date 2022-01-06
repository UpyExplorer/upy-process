# coding=utf-8

"""
Model Config
"""

from app import db, ma
from marshmallow import fields, EXCLUDE
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)

class WorkStation(Base):

    __tablename__ = 'work_station'

    key = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    ip_address = db.Column(db.String(15), nullable=True)
    port = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer, nullable=True)

    def __init__(
        self,
        key,
        description=None,
        ip_address=None,
        port=None,
        status=None):

        self.key = key
        self.description = description
        self.ip_address = ip_address
        self.port = port
        self.status = status

    def __repr__(self):
        return '<id %r>' % (self.id)

class WorkStationSchema(ma.Schema):
    key = fields.Str()
    description = fields.Str()
    ip_address = fields.Str()
    port = fields.Integer()
    status = fields.Integer()

    class Meta:
        unknown = EXCLUDE
        fields = (
            'id',
            'key',
            'description',
            'ip_address',
            'port',
            'status'
        )

base_schema = WorkStationSchema()
base_schemas = WorkStationSchema(many=True)