"""
Define the Wine Category model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database


class WineCategory(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Wine Category model"""

    __tablename__ = "category"
    __table_args__ = {
        Database.ENGINE_KEY: Database.ENGINE_VALUE,
        Database.CHARSET_KEY: Database.CHARSET_VALUE,
        Database.COLLATION_KEY: Database.COLLATION_VALUE,
    }

    id = db.Column(
        db.BigInteger(), primary_key=True, nullable=False, comment="Primary key"
    )
    main_category_id = db.Column(
        db.BigInteger(), nullable=False, comment="Main category id"
    )
    name = db.Column(db.String(50), nullable=True, comment="Category name")
