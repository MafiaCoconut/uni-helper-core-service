from application.interfaces.telegram_interface import TelegramInterface
from infrastructure.config.logs_config import log_decorator


class SendCanteensMenuUseCase:
    def __init__(self,
                 telegram_interface: TelegramInterface
                 ):
        self.telegram_interface = telegram_interface

    @log_decorator(print_args=False, print_kwargs=False)
    async def execute(self, user_id: int, message: str, keyboard):
        await self.telegram_interface.send_message(user_id=user_id, message=message, keyboard=keyboard)

