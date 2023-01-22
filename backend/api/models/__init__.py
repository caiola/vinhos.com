from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .users import User
from .ads import Ad
