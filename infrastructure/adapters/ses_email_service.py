import boto3

from adapters.email_sender_gateway import EmailSenderGateway


class SesEmailService(EmailSenderGateway):
    def __init__(self) -> None:
        self.__simple_email_service = boto3.client(
            'ses', region_name='sa-east-1'
        )

    def send(self, to: str, subject: str, body: str) -> None:
        self.__simple_email_service.send_email(
            Source='jacksonsr45@gmail.com',
            Destination={
                'ToAddresses': [
                    to,
                ]
            },
            Message={
                'Subject': {'Data': subject, 'Charset': 'utf-8'},
                'Body': {'Text': {'Data': body, 'Charset': 'utf-8'}},
            },
        )
