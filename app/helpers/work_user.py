# coding=utf-8

__all__ = ['WorkUserHelper']

from app.helpers.base import ControlerBase
from app.models.work_user import WorkUser, base_schema, base_schemas


class WorkUserHelper(ControlerBase):
    """WorkUser Helper
    """
    def __init__(self, data=None):
        super().__init__()

        self.model_class = WorkUser
        self.base_schema = base_schema
        self.base_schemas = base_schemas
