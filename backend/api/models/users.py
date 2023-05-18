"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The User model"""

    __tablename__ = "users"

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
