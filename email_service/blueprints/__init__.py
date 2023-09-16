from flask import Flask

from .api.emails import email_bp


def init_app(app: Flask) -> None:
    app.register_blueprint(email_bp)
