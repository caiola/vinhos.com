"""
Define the Address model
"""
from enum import Enum

from . import db
from .abc import BaseModel, MetaBaseModel
from .address_type import AddressType
from .database import Database
from .status_type import StatusType
from .utils import lowercase_enum


class Address(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Address model"""

    __tablename__ = "address"
    __table_args__ = {
        Database.ENGINE_KEY: Database.ENGINE_VALUE,
        Database.CHARSET_KEY: Database.CHARSET_VALUE,
        Database.COLLATION_KEY: Database.COLLATION_VALUE,
    }

    id = db.Column(
        db.BigInteger(), primary_key=True, nullable=False, comment="Primary key"
    )
    status_id = db.Column(
        db.Integer(), default=StatusType.NEW, nullable=False, comment="Status id"
    )

    account_id = db.Column(
        db.BigInteger(),
        nullable=True,
        index=True,
        comment="Associate address with Account id",
    )
    store_id = db.Column(
        db.BigInteger(),
        nullable=True,
        index=True,
        comment="Associate address with Store id",
    )
    user_id = db.Column(
        db.BigInteger(),
        nullable=True,
        index=True,
        comment="Associate address with User id",
    )

    address_type = db.Column(
        lowercase_enum(AddressType),
        nullable=False,
        comment="Address type (e.g. account,store,user,billing,pickup)",
    )
    designation = db.Column(
        db.String(50),
        nullable=True,
        comment="Designation is the internal name of the address",
    )
    is_default_address = db.Column(
        db.SmallInteger(),
        nullable=True,
        index=True,
        comment="Is default address e.g. 0=No; 1=Yes",
    )

    country = db.Column(db.String(2), nullable=True, comment="Country alpha2")

    district = db.Column(db.String(50), nullable=True, comment="District name")

    municipality = db.Column(db.String(50), nullable=True, comment="Municipality name")

    parish = db.Column(db.String(50), nullable=True, comment="Parish name")

    zone = db.Column(db.String(50), nullable=True, comment="Zone")

    street = db.Column(db.String(50), nullable=True, comment="Street name")

    floor = db.Column(db.String(50), nullable=True, comment="Floor")
    number = db.Column(db.String(50), nullable=True, comment="Number")

    postal_code = db.Column(db.String(50), nullable=True, comment="Postal code")
    additional_details = db.Column(
        db.String(250), nullable=True, comment="Additional details e.g. known places"
    )

    email = db.Column(db.String(50), nullable=True, comment="Email")
    phone = db.Column(db.String(50), nullable=True, comment="Phone")
    phone_secondary = db.Column(db.String(50), nullable=True, comment="Phone secondary")
    fax = db.Column(db.String(50), nullable=True, comment="Fax")
    person = db.Column(
        db.String(50), nullable=True, comment="Person responsible on this address"
    )
