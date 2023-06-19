"""
Define the Address model
"""
from enum import Enum

from . import db
from .abc import BaseModel, MetaBaseModel
from .address_type import AddressType
from .database import Database
from .status_type import StatusType


def lowercase_enum(enum_class):
    return db.Enum(*(item.value.lower() for item in enum_class), name="lowercase_enum")


class Address(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Address model"""

    __tablename__ = "address"
    __table_args__ = {
        Database.ENGINE_KEY: Database.ENGINE_VALUE,
        Database.CHARSET_KEY: Database.CHARSET_VALUE,
        Database.COLLATION_KEY: Database.COLLATION_VALUE,
    }

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False, comment="Primary key")
    status_id = db.Column(db.Integer(), default=StatusType.NEW, nullable=False, comment="Status id")

    account_id = db.Column(db.BigInteger(), nullable=True, index=True, comment="Associate address with Account id")
    store_id = db.Column(db.BigInteger(), nullable=True, index=True, comment="Associate address with Store id")
    user_id = db.Column(db.BigInteger(), nullable=True, index=True, comment="Associate address with User id")

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
        db.SmallInteger(), nullable=True, index=True, comment="Is default address e.g. 0=No; 1=Yes"
    )

    # country_id = db.Column(db.BigInteger(), nullable=True, comment="Country id")
    country = db.Column(db.String(2), nullable=True, comment="Country alpha2")

    # district_id = db.Column(db.BigInteger(), nullable=True, comment="District id")
    district = db.Column(db.String(50), nullable=True, comment="District name")

    # municipality_id = db.Column(db.BigInteger(), nullable=True, comment="Municipality id")
    municipality = db.Column(db.String(50), nullable=True, comment="Municipality name")

    # parish_id = db.Column(db.BigInteger(), nullable=True, comment="Parish id")
    parish = db.Column(db.String(50), nullable=True, comment="Parish name")

    zone = db.Column(db.String(50), nullable=True, comment="Zone")

    # street_id = db.Column(db.BigInteger(), nullable=True, comment="Street id")
    street = db.Column(db.String(50), nullable=True, comment="Street name")

    floor = db.Column(db.String(50), nullable=True, comment="Floor")
    number = db.Column(db.String(50), nullable=True, comment="Number")

    postal_code = db.Column(db.String(50), nullable=True, comment="Postal code")
    additional_details = db.Column(db.String(250), nullable=True, comment="Additional details e.g. known places")

    email = db.Column(db.String(50), nullable=True, comment="Email")
    phone = db.Column(db.String(50), nullable=True, comment="Phone")
    phone_secondary = db.Column(db.String(50), nullable=True, comment="Phone secondary")
    fax = db.Column(db.String(50), nullable=True, comment="Fax")
    person = db.Column(
        db.String(50), nullable=True, comment="Person responsible on this address"
    )
