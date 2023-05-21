"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from .address_type import AddressType
from .database import Database
from .status_type import StatusType


class Address(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Address model"""

    __tablename__ = "address"
    __table_args__ = {Database.ENGINE_KEY: Database.ENGINE_VALUE, Database.CHARSET_KEY: Database.CHARSET_VALUE,
                      Database.COLLATION_KEY: Database.COLLATION_VALUE}

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False, comment="Primary key")
    id_status = db.Column(db.Integer(), default=StatusType.NEW, nullable=False, comment="Status id")

    address_type = db.Column(db.Enum([e.value for e in AddressType], name='address_type'), nullable=False,
                             comment="Address type")

    account_id = db.Column(db.BigInteger(), nullable=True, comment="Associate address with Account id")
    store_id = db.Column(db.BigInteger(), nullable=True, comment="Associate address with Store id")
    user_id = db.Column(db.BigInteger(), nullable=True, comment="Associate address with User id")

    country_id = db.Column(db.BigInteger(), nullable=True, comment="Country id")
    country = db.Column(db.String(50), nullable=True, comment="Country name")

    district_id = db.Column(db.BigInteger(), nullable=True, comment="District id")
    district = db.Column(db.String(50), nullable=True, comment="District name")

    municipality_id = db.Column(db.BigInteger(), nullable=True, comment="Municipality id")
    municipality = db.Column(db.String(50), nullable=True, comment="Municipality name")

    parish_id = db.Column(db.BigInteger(), nullable=True, comment="Parish id")
    parish = db.Column(db.String(50), nullable=True, comment="Parish name")

    zone = db.Column(db.String(50), nullable=True, comment="Zone")

    street_id = db.Column(db.BigInteger(), nullable=True, comment="Street id")
    street = db.Column(db.String(50), nullable=True, comment="Street name")

    floor = db.Column(db.String(50), nullable=True, comment="Floor")
    number = db.Column(db.String(50), nullable=True, comment="Number")

    postal_code = db.Column(db.String(50), nullable=True, comment="Postal code")
    additional_details = db.Column(db.String(250), nullable=True, comment="Additional details e.g. known places")
