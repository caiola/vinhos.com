import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from api.config import DB_URI

db = SQLAlchemy()
engine = sqlalchemy.create_engine(DB_URI)

from .abc import BaseModel
from .ads import Ad
from .users import User
from .accounts import Account
