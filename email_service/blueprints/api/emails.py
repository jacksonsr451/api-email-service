from flask import Blueprint, Response, request
from controllers import email_controller

from controllers.email_controller import EmailController

email_bp = Blueprint('email', __name__, url_prefix='/api/v1/email')

controller_instance: EmailController


def init_controller(email_controller: EmailController) -> None:
    global controller_instance
    controller_instance = email_controller


@email_bp.route('/', methods=['POST'])
def send_email() -> Response:
    request_data = request.get_json()
    return controller_instance.send(
        to=request_data['to'],
        subject=request_data['subject'],
        body=request_data['body'],
    )
