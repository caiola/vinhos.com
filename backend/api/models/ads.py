"""
Define the Add model
"""
import uuid
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, UniqueConstraint

from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database
from .status_type import StatusType


class Ad(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Ad model"""

    __tablename__ = "ad"

    __table_args__ = (
        # Ad title is unique by account, which means is unique through all stores of the account
        UniqueConstraint('account_id', 'title', name='ad_unique_account_id_and_title'),
        {Database.ENGINE_KEY: Database.ENGINE_VALUE, Database.CHARSET_KEY: Database.CHARSET_VALUE,
         Database.COLLATION_KEY: Database.COLLATION_VALUE},
    )

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False, comment="Primary key")
    status_id = db.Column(db.Integer(), default=StatusType.NEW.value, nullable=False, comment="Status id")
    address_id = db.Column(db.BigInteger(), nullable=False, comment="Address id")
    uuid = db.Column(db.String(36), default=uuid.uuid4, unique=True, nullable=False, comment="UUID")

    title = db.Column(db.String(100), nullable=False, comment="Title")
    description = db.Column(db.Text(), nullable=False, comment="Description")

    account_id = Column(db.BigInteger(),
                        ForeignKey('account.id', name="ad_account_id_fk_account_id",
                                   onupdate="RESTRICT", ondelete="RESTRICT"), nullable=False, comment="Account id")
    store_id = Column(db.BigInteger(),
                      ForeignKey('store.id', name="ad_store_id_fk_store_id", onupdate="RESTRICT",
                                 ondelete="RESTRICT"), nullable=False, comment="Store id")
    user_id = Column(db.BigInteger(),
                     ForeignKey('user.id', name="ads_user_id_fk_user_id", onupdate="RESTRICT",
                                ondelete="RESTRICT"), nullable=False, comment="User id")

    user = db.relationship('User', backref=db.backref('ad', lazy=True))
    store = db.relationship('Store', backref=db.backref('ad', lazy=True))
    account = db.relationship('Account', backref=db.backref('ad', lazy=True))
