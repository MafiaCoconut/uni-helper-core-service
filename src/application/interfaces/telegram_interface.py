from abc import ABC, abstractmethod


class TelegramInterface(ABC):
    @staticmethod
    @abstractmethod
    def send_message(user_id: int, message: str, keyboard: None):
        pass
