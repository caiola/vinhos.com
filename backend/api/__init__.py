"""Application entrypoint"""
import os

from flask import Flask
from flask_migrate import Migrate

from api.models import db
from api.resources.ads import blueprint as ads_blueprint
from flask_jwt_extended import JWTManager



def create_app(test_config=None):


    """Creates a Flask instance"""
    app = Flask(__name__)
    app.config.from_object("api.config")
    app.debug = config.DEBUG
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

    # Set your own secret key
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
    jwt = JWTManager(app)

    db.init_app(app)
    Migrate(app, db)

    # Route registration
    app.register_blueprint(ads_blueprint)

    return app

