"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database
from .status_type import StatusType


class Account(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Account model"""

    __tablename__ = "account"
    __table_args__ = {Database.ENGINE_KEY: Database.ENGINE_VALUE, Database.CHARSET_KEY: Database.CHARSET_VALUE,
                      Database.COLLATION_KEY: Database.COLLATION_VALUE}

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    status_id = db.Column(db.Integer(), default=StatusType.NEW, nullable=False, comment="Status id")
    address_id = db.Column(db.BigInteger(), nullable=False, comment="Address id")

    account_name = db.Column(db.String(50), unique=True, nullable=False)

    nif = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    company_name = db.Column(db.String(50), nullable=False)
