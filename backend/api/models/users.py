"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "users"

    id = db.Column(db.BigInteger(), primary_key=True)
    first_name = db.Column(db.String(300), primary_key=True)
    last_name = db.Column(db.String(300), primary_key=True)
    age = db.Column(db.Integer, nullable=True)

    def __init__(self, id, first_name, last_name, age=None):
        """ Create a new User """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
