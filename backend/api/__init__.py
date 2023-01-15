
from flasgger import Swagger
from flask import Flask
from flask.blueprints import Blueprint
from api.models import db
from api import routes
from flask_migrate import Migrate

def create_app(test_config=None):

	app = Flask(__name__)
	app.config.from_object('api.config')
	app.config["SWAGGER"] = {
	    "swagger_version": "2.0",
	    "title": "Application",
	    "specs": [
	        {
	            "version": "0.0.1",
	            "title": "Application",
	            "endpoint": "spec",
	            "route": "/application/spec",
	            "rule_filter": lambda rule: True,  # all in
	        }
	    ],
	    "static_url_path": "/apidocs",
	}

	Swagger(app)
	app.debug = config.DEBUG
	app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
	db.init_app(app)
	Migrate(app, db)

	# Route registration
	app.register_blueprint(routes.USER_BLUEPRINT)

	return app
