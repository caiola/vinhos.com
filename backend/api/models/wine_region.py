"""
Define the Wine Region model
"""
from flask import json

from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database



class WineRegion(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Wine Region model"""

    __tablename__ = "region"
    __table_args__ = {Database.ENGINE_KEY: Database.ENGINE_VALUE, Database.CHARSET_KEY: Database.CHARSET_VALUE,
                      Database.COLLATION_KEY: Database.COLLATION_VALUE}

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False, comment="Primary key")
    country = db.Column(db.String(2), nullable=False, comment="Country")
    name = db.Column(db.String(50), nullable=True, comment="Name of region")

    # def toJson(self):
    #     return json.dumps(self, default=lambda o: o.__dict__,
    #                       sort_keys=True, indent=4)
