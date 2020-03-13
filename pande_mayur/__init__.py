from flask import Flask
from .views.address import address


def create_app():
    """Create app function to handle instantiation of Flask app and to be able to use outside of context if needed"""

    app = Flask(__name__)

    app.register_blueprint(address)

    return app
