from flask import Blueprint, Response, request

from application.email_sender_service import EmailSenderService
from controllers.email_controller import EmailController
from infrastructure.adapters.ses_email_service import SesEmailService

email_bp = Blueprint('email', __name__, url_prefix='/api/v1/email')

email_sender = SesEmailService()
email_service = EmailSenderService(email_sender_gateway=email_sender)
email_controller = EmailController(email_service=email_service)


@email_bp.route('/', methods=['POST'])
def send_email() -> Response:
    request_data = request.get_json()
    return email_controller.send(
        to=request_data['to'],
        subject=request_data['subject'],
        body=request_data['body'],
    )
