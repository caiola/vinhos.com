"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Account(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Account model"""

    __tablename__ = "accounts"

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    account_name = db.Column(db.String(50), unique=True, nullable=False)
    company_name = db.Column(db.String(50), nullable=False)
