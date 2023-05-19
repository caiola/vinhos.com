"""
Define the Store model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Stores(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Stores model"""

    __tablename__ = "stores"

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    store_name = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    municipality = db.Column(db.String(50), nullable=False)
    parish = db.Column(db.String(50), nullable=False)
    zone = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(50), nullable=False)
