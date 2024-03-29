"""
Define an Abstract Base Class (ABC) for models
"""
from datetime import datetime

from flask import abort
from sqlalchemy import inspect
from sqlalchemy.orm import declarative_base

from . import db

# from weakref import WeakValueDictionary


# class MetaBaseModel(db.Model.__class__):
#     """Define a metaclass for the BaseModel
#     Implement `__getitem__` for managing aliases"""
#
#     def __init__(cls, *args):
#         super().__init__(*args)
#         cls.aliases = WeakValueDictionary()
#
#     def __getitem__(cls, key):
#         try:
#             alias = cls.aliases[key]
#         except KeyError:
#             alias = aliased(cls)
#             cls.aliases[key] = alias
#         return alias


class MetaBaseModel(db.Model.__class__):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._meta = {}
        for key, value in attrs.items():
            if isinstance(value, str):
                cls._meta[key] = value


class BaseModel:
    """Generalize __init__, __repr__ and to_json
    Based on the models columns"""

    print_filter = ()
    to_json_filter = ()

    # def __repr__(self):
    #     """Define a base way to print models
    #     Columns inside `print_filter` are excluded"""
    #     return "%s(%s)" % (
    #         self.__class__.__name__,
    #         {
    #             column: value
    #             for column, value in self._to_dict().items()
    #             if column not in self.print_filter
    #         },
    #     )
    # def __repr__(self):
    #     """Override __repr__ to display the object representation"""
    #     return f"{self.__class__.__name__}({self._to_dict()})"

    # def __repr__(self):
    #     class_name = self.__class__.__name__
    #     properties = [
    #         f"{key}={repr(getattr(self, key))}" for key in inspect(self.__class__).attrs
    #     ]
    #     return f"{class_name}({', '.join(properties)})"

    # @property
    # def json(self):
    #     """Define a base way to jsonify models
    #     Columns inside `to_json_filter` are excluded"""
    #     return {
    #         column: value
    #         if not isinstance(value, datetime)
    #         else value.strftime("%Y-%m-%d")
    #         for column, value in self._to_dict().items()
    #         if column not in self.to_json_filter
    #     }
    #
    # def _to_dict(self):
    #     """This would more or less be the same as a `to_json`
    #     But putting it in a "private" function
    #     Allows to_json to be overriden without impacting __repr__
    #     Or the other way around
    #     And to add filter lists"""
    #     return {
    #         column.key: getattr(self, column.key)
    #         for column in inspect(self.__class__).attrs
    #     }
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = [
            f"{key}={repr(getattr(self, key))}" for key in self._to_dict().keys()
        ]
        return f"{class_name}({', '.join(properties)})"

    @property
    def json(self):
        """Define a base way to jsonify models
        Columns inside `to_json_filter` are excluded"""
        return {
            column: value
            if not isinstance(value, datetime)
            else value.strftime("%Y-%m-%d")
            for column, value in self._to_dict().items()
            if column not in self.to_json_filter
        }

    def _to_dict(self):
        """This would more or less be the same as a `to_json`
        But putting it in a "private" function
        Allows to_json to be overridden without impacting __repr__
        Or the other way around
        And to add filter lists"""
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self.__class__).attrs
        }

    def save(self, refresh=False):
        try:
            db.session.add(self)
            db.session.commit()
            if refresh:
                db.session.refresh(self)
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
        return self

    def update(self, data):  # Built-in signature is => def update(self, E=None, **F):
        db.session.update(self, data)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# BaseModel = declarative_base(cls=BaseModel, metaclass=MetaBaseModel)
