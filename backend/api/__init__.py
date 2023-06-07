"""Application entrypoint"""
import os

from flask import Flask, app
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from sqlalchemy.engine import Engine

from api.models import db
from api.resources.accounts import blueprint as accounts_blueprint
from api.resources.stores import blueprint as stores_blueprint
from api.resources.users import blueprint as users_blueprint
from api.resources.ads import blueprint as ads_blueprint
from api.resources.regions import blueprint as regions_blueprint
from api.resources.categories import blueprint as categories_blueprint
from api.resources.auth import blueprint as auth_blueprint
from seeds.seed import seed_tables


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
    app.register_blueprint(accounts_blueprint)
    app.register_blueprint(stores_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(ads_blueprint)
    app.register_blueprint(regions_blueprint)
    app.register_blueprint(categories_blueprint)
    app.register_blueprint(auth_blueprint)

    return app


app = create_app()


@app.cli.command("seed_db")
def seed_db():
    with app.app_context():
        seed_tables(app)
