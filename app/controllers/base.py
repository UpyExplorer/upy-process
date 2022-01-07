# coding=utf-8

"""
Module Docstring
"""

__all__ = ['ControlerBase']

from app import db


class ControlerBase(object):
    """Controle Base
    """
    def __init__(self):
        """Constructor Class
        """
        self.model_class = None
        self.base_schema = None
        self.base_schemas = None
        self.db_session = db.session

    def get_all(self):
        """Returns all database information
        Returns:
            query_data (dict or None): Returns a dictionary or None
        """
        try:
            query_data = self.model_class.query.all()
            
            if query_data:
                return self.base_schemas.dump(query_data) or None

        except Exception as error:
            print(error)
            self.db_session.rollback()
            
        return None

    def get(self, model_id=None):
        """Returns database information
        Args:
            model_id (int, optional): Defaults to None.
        Returns:
            query_data (dict or None): Returns a dictionary or None
        """
        try:
            query_data = self.model_class.query \
                .filter(
                    self.model_class.id == model_id
                ).first()
                
            if query_data:
                return self.base_schema.dump(query_data) or None
            
        except Exception as error:
            print(error)
            self.db_session.rollback()

        return None

    def upsert(self, model_id=None, data=None):
        """Edit or update records
        Args:
            model_id ([int, optional): Defaults to None.
            data (dict, optional): Defaults to None.
        Returns:
            model: SQLAlchemy
        """
        model = self.model_class.query.filter(
            self.model_class.id == model_id
        ).first()

        is_new = model is None

        try:
            if is_new:
                model = self.model_class(**data)
                self.db_session.add(model)
            else:
                for item in data:
                    setattr(model, item, data[item])
                self.db_session.merge(model)

            self.db_session.commit()
            return model
        except:
            self.db_session.rollback()

        return None

    def delete(self, model_id=None):
        """Delete a record
        Args:
            model_id (int, optional): Defaults to None.
        Returns:
            bool: Return True or False
        """
        try:
            model = self.model_class.query \
                .filter(
                    self.model_class.id == model_id
                ).first()
            
            self.db_session.delete(model)
            self.db_session.commit()
            
            return True
        except:
            self.db_session.rollback()

        return False
