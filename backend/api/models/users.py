"""
Define the User model
"""
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database
from .status_type import StatusType


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The User model"""

    __tablename__ = "user"
    __table_args__ = {Database.ENGINE_KEY: Database.ENGINE_VALUE, Database.CHARSET_KEY: Database.CHARSET_VALUE,
                      Database.COLLATION_KEY: Database.COLLATION_VALUE}

    id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    status_id = db.Column(db.Integer(), default=StatusType.NEW, nullable=False, comment="Status id")

    first_name = db.Column(db.String(150), nullable=False, comment="First name")
    middle_name = db.Column(db.String(150), nullable=False, comment="Middle name")
    last_name = db.Column(db.String(150), nullable=False, comment="Last name")

    password_hash = db.Column(db.String(128), nullable=False, comment="Password hash")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
