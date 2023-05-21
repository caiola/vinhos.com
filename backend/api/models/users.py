"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database
from .status_type import StatusType


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The User model"""

    __tablename__ = "users"
    __table_args__ = {Database.ENGINE_KEY: Database.ENGINE_VALUE, Database.CHARSET_KEY: Database.CHARSET_VALUE,
                      Database.COLLATION_KEY: Database.COLLATION_VALUE}

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    id_status = db.Column(db.Integer(), default=StatusType.NEW, nullable=False, comment="Status id")
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
