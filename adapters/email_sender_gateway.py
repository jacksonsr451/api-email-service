from abc import ABC, abstractmethod


class EmailSenderGateway(ABC):
    @abstractmethod
    def send(self, to: str, subject: str, body: str) -> None:
        pass
