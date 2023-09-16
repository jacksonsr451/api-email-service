from flask import Flask

from email_service import blueprints
from email_service.blueprints.api import emails
from email_service.factories.email_controller_factory import email_controller_factory
from infrastructure.adapters.ses_email_service import SesEmailService


def create_app() -> Flask:
    app = Flask(__name__)

    emails.init_controller(email_controller_factory(SesEmailService()))

    blueprints.init_app(app)

    return app
