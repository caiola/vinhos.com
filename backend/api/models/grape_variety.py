"""
Define the Status Type model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database


class GrapeVariety(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Grape Varieties model"""

    __tablename__ = "grape_variety"
    __table_args__ = {Database.ENGINE_KEY: Database.ENGINE_VALUE, Database.CHARSET_KEY: Database.CHARSET_VALUE,
                      Database.COLLATION_KEY: Database.COLLATION_VALUE}

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False, comment="Primary key")
    grape_variety = db.Column(db.String(50), nullable=True, comment="Grape variety")
