from abc import ABC, abstractmethod


class TelegramInterface(ABC):
    @staticmethod
    @abstractmethod
    async def send_message(user_id: int, message: str, keyboard: None):
        pass

    @staticmethod
    @abstractmethod
    async def send_message_to_admin(message: str, keyboard: None):
        pass

    @staticmethod
    @abstractmethod
    async def edit_message_with_callback(callback, message: str, keyboard: None):
        pass

