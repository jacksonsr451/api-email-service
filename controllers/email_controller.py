from flask import jsonify

from application.email_sender_service import EmailSenderService


class EmailController:
    def __init__(self, email_service: EmailSenderService):
        self.__email_service: EmailSenderService = email_service

    def send(self, to: str, subject: str, body: str):
        try:
            self.__email_service.send(to, subject, body)
            return jsonify({'message': 'Email sent'})
        except Exception as e:
            return jsonify({'message': str(e)}), 400
