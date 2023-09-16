import unittest
from flask import Flask
from adapters.email_sender_gateway import EmailSenderGateway
from email_service import blueprints
from email_service.blueprints.api import emails
from email_service.factories.email_controller_factory import email_controller_factory


class MockSesEmailService(EmailSenderGateway):
    def send(self, to, subject, body):
        return True


class TestEmailController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

        emails.init_controller(
            email_controller_factory(MockSesEmailService()))
        blueprints.init_app(self.app)

        self.client = self.app.test_client()

        self.app.config['TESTING'] = True

    def test_send_email(self):
        response = self.client.post('/api/v1/email/', json={
            'to': 'recipient@example.com',
            'subject': 'Test Subject',
            'body': 'Test Body',
        })

        self.assertEqual(response.status_code, 200)
