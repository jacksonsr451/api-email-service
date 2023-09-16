from adapters.email_sender_gateway import EmailSenderGateway
from application.email_sender_service import EmailSenderService
from controllers.email_controller import EmailController


def email_controller_factory(email_gateway: EmailSenderGateway) -> EmailController:
    email_service = EmailSenderService(email_sender_gateway=email_gateway)
    return EmailController(email_service)
