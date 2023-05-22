"""
Define the Store model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database
from .status_type import StatusType


class Store(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Store model"""

    __tablename__ = "store"
    __table_args__ = {Database.ENGINE_KEY: Database.ENGINE_VALUE, Database.CHARSET_KEY: Database.CHARSET_VALUE,
                      Database.COLLATION_KEY: Database.COLLATION_VALUE}

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    status_id = db.Column(db.Integer(), default=StatusType.NEW, nullable=False, comment="Status id")
    account_id = db.Column(db.Integer(), default=StatusType.NEW, nullable=False, comment="Account id")
    address_id = db.Column(db.BigInteger(), nullable=False, comment="Address id")

    store_name = db.Column(db.String(50), nullable=False, comment="Store name")

    gps_latitude = db.Column(db.String(25), nullable=False, comment="GPS coordinates, latitude")
    gps_longitude = db.Column(db.String(25), nullable=False, comment="GPS coordinates, longitude")

    contact_email = db.Column(db.String(50), nullable=False, comment="Email")

    contact_phone = db.Column(db.String(50), nullable=False, comment="Phone")
    contact_phone_description = db.Column(db.String(50), nullable=False, comment="Phone description (e.g. call to land line)")

    contact_phone_secondary = db.Column(db.String(50), nullable=False, comment="Secondary phone")
    contact_phone_secondary_description = db.Column(db.String(50), nullable=False,
                                                    comment="Secondary phone description (e.g. mobile phone)")

    schedule = db.Column(db.String(50), nullable=False, comment="Open hours (e.g. Open 8h to 24h, Mon to Sat)")

    social_facebook = db.Column(db.String(50), nullable=False, comment="Address for social network Facebook")
    social_twitter = db.Column(db.String(50), nullable=False, comment="Address for social network Twitter")
    social_instagram = db.Column(db.String(50), nullable=False, comment="Address for social network Instagram")
    social_tiktok = db.Column(db.String(50), nullable=False, comment="Address for social network Tiktok")
