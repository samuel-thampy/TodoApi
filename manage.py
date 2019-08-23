from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

import src.config as config
from src.extensions import db

app = Flask(__name__)
app.debug = config.DEBUG
app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
