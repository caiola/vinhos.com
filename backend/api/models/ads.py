"""
Define the Add model
"""
import uuid
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, UniqueConstraint

from . import db
from .abc import BaseModel, MetaBaseModel


class Ad(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Ad model"""

    __tablename__ = "ads"

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    uuid = db.Column(db.String(36), default=uuid.uuid4, unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    user_id = Column(db.BigInteger(), ForeignKey('users.id', name="ads_user_id_fk_users_id", onupdate="RESTRICT",
                                                 ondelete="RESTRICT"), nullable=False)

    user = relationship("User")

    __table_args__ = (
        UniqueConstraint('id', 'title', name='uq_id_title'),
    )