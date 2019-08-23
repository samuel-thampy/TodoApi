from flasgger import Swagger
from flask import Flask
from flask.blueprints import Blueprint
import os

from src.extensions import db

import src.config as config
import src.routes as routes


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

