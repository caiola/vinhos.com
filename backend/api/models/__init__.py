import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from api.config import DB_URI

db = SQLAlchemy()
engine = sqlalchemy.create_engine(DB_URI)

from .abc import BaseModel
from .accounts import Account
from .stores import Store
from .users import User
from .ads import Ad
