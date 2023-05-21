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
    __table_args__ = {Database.ENGINE_KEY: Database.ENGINE_VALUE, Database.CHARSET_KEY: Database.CHARSET_VALUE,
                      Database.COLLATION_KEY: Database.COLLATION_VALUE}

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False, comment="Primary key")
    id_status = db.Column(db.Integer(), default=StatusType.NEW, nullable=False, comment="Status id")
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

    user = relationship("User")

    __table_args__ = (
        UniqueConstraint('id', 'title', name='ad_unique_id_title'),
    )
