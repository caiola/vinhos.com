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
    __table_args__ = {
        Database.ENGINE_KEY: Database.ENGINE_VALUE,
        Database.CHARSET_KEY: Database.CHARSET_VALUE,
        Database.COLLATION_KEY: Database.COLLATION_VALUE,
    }

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    status_id = db.Column(
        db.Integer(), default=StatusType.NEW, nullable=False, comment="Status id"
    )
    address_id = db.Column(db.BigInteger(), nullable=True, comment="Address id")

    account_name = db.Column(
        db.String(60),
        nullable=True,
        comment="Account can have any name, it is an internal reference",
    )

    # Tax information
    country = db.Column(db.String(2), nullable=True)
    company_name = db.Column(db.String(50), nullable=True)
    tax_number = db.Column(db.String(50), nullable=True)
