"""
Define the Add model
"""
import uuid
from sqlalchemy.orm import declarative_base, relationship

from . import db
from .abc import BaseModel, MetaBaseModel


class Ad(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Ad model"""

    __tablename__ = "ads"

    id = db.Column(db.BigInteger(), primary_key=True)
    uuid = db.Column(db.String(50), default=uuid.uuid4, unique=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"), nullable=False)

    user = relationship("User")
