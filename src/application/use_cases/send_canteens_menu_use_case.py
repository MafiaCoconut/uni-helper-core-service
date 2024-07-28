from application.interfaces.telegram_interface import TelegramInterface


class SendCanteensMenuUseCase:
    def __init__(self,
                 telegram_interface: TelegramInterface
                 ):
        self.telegram_interface = telegram_interface

    def execute(self, user_id: int, message: str, keyboard):
        self.telegram_interface.send_message(user_id=user_id, message=message, keyboard=keyboard)

