from flask import Flask

from email_service import blueprints


def create_app() -> Flask:
    app = Flask(__name__)
    blueprints.init_app(app)
    return app
