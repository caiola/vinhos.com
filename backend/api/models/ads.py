"""
Define the Add model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
import uuid

class Ad(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Ad model """

    __tablename__ = "ads"

    id = db.Column(db.BigInteger(), primary_key=True)
    uuid = db.Column(db.String(32), default=uuid.uuid4)
    title = db.Column(db.String(100), primary_key=False)
    description = db.Column(db.Text(), primary_key=False)

    def __init__(self, id, uuid, title, description):
        """ Create a ad """
        self.id = id
        self.uuid = uuid
        self.title = title
        self.description = description
