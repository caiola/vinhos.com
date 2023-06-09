"""
Define the Status model
"""

from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database


class Status(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Status model"""

    __tablename__ = "status"
    __table_args__ = {
        Database.ENGINE_KEY: Database.ENGINE_VALUE,
        Database.CHARSET_KEY: Database.CHARSET_VALUE,
        Database.COLLATION_KEY: Database.COLLATION_VALUE,
    }

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
