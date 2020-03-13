from flask import Flask
from .views.address import address
from .extensions import db, migrate
from .models.models import *
from .config import Config


def create_app():
    """Create app function to handle instantiation of Flask app and to be able to use outside of context if needed"""

    app = Flask(__name__)

    # set config for app from Config class
    app.config.from_object(Config)

    # init db on app
    db.init_app(app)
    # init migrate to app using db
    migrate.init_app(app, db)

    # register blueprints to app
    app.register_blueprint(address)

    return app
