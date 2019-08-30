from flasgger import Swagger
from flask import Flask
from flask.blueprints import Blueprint
import os

from .extensions import db

from .routes import *
from .config import *


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

app.debug = DEBUG
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)
db.app = app

for blueprint in vars(routes).values():

    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=APPLICATION_ROOT)
