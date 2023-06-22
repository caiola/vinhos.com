"""
Define the Verification model

This is used to make verifications e.g. account registration verification of the token sent by email
"""
from sqlalchemy import UniqueConstraint, func

from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database
from .utils import lowercase_enum
from .verification_type import VerificationType


class Verification(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Verification model"""

    __tablename__ = "verification"
    __table_args__ = (
        UniqueConstraint("user_id", "type", "token", name="ad_user_type_token"),
        {
            Database.ENGINE_KEY: Database.ENGINE_VALUE,
            Database.CHARSET_KEY: Database.CHARSET_VALUE,
            Database.COLLATION_KEY: Database.COLLATION_VALUE,
        },
    )

    id = db.Column(
        db.BigInteger(), primary_key=True, nullable=False, comment="Primary key"
    )
    user_id = db.Column(db.BigInteger(), nullable=False, comment="User id")
    type = db.Column(
        lowercase_enum(db.Enum, VerificationType),
        nullable=False,
        comment="Verification type (e.g. user,email,otp)",
    )
    token = db.Column(
        db.String(64), nullable=False, unique=True, comment="Unique token"
    )
    date_created = db.Column(
        db.DateTime(timezone=True),
        default=func.utcnow(),
        comment="Date when token was created",
    )
