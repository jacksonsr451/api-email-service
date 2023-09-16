from adapters.email_sender_gateway import EmailSenderGateway
from core.email_sender_use_case import EmailSenderUseCase


class EmailSenderService(EmailSenderUseCase):
    __email_sender_gateway: EmailSenderGateway

    def __init__(self, email_sender_gateway: EmailSenderGateway) -> None:
        self.__email_sender_gateway = email_sender_gateway

    def send(self, to: str, subject: str, body: str) -> None:
        self.__email_sender_gateway.send(to, subject, body)
