from abc import ABC, abstractmethod


class EmailSenderUseCase(ABC):
    @abstractmethod
    def send(to: str, subject: str, body: str) -> None:
        pass
