"""
Define the Wine Type model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database


class WineType(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Wine Type model"""

    __tablename__ = "type"
    __table_args__ = {Database.ENGINE_KEY: Database.ENGINE_VALUE, Database.CHARSET_KEY: Database.CHARSET_VALUE,
                      Database.COLLATION_KEY: Database.COLLATION_VALUE}

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False, comment="Primary key")
    name = db.Column(db.String(50), nullable=True, comment="Name of wine type")
