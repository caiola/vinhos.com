# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello():
#     return "<h1 style='color:blue'>Hello There!</h1>"
#
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0')


from flasgger import Swagger
from flask import Flask
from flask.blueprints import Blueprint

import config
import routes
from models import db

# config your API specs
# you can define multiple specs in the case your api has multiple versions
# ommit configs to get the default (all views exposed in /spec url)
# rule_filter is a callable that receives "Rule" object and
#   returns a boolean to filter in only desired views

app = Flask(__name__)

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
db.app = app

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
     app.run(host=config.HOST, port=config.PORT)
