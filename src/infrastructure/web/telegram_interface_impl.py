from application.interfaces.telegram_interface import TelegramInterface


class TelegramInterfaceImpl(TelegramInterface):
    @staticmethod
    def send_message(user_id: int, message: str, keyboard: None):
        pass
