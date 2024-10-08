from application.interfaces.telegram_interface import TelegramInterface
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder
from infrastructure.config.logs_config import log_decorator


class AdminMenuUseCase:
    def __init__(self,
                 admin_menu_keyboards: AdminMenuKeyboardsBuilder,
                 telegram_interface: TelegramInterface,
                 ):
        self.admin_menu_keyboards = admin_menu_keyboards
        self.telegram_interface = telegram_interface

    @log_decorator(print_args=False, print_kwargs=False)
    async def send_menu_main(self, user_id: int):
        await self.telegram_interface.send_message(
            user_id=user_id,
            message="<b>Меню администратора</b>",
            keyboard=await self.admin_menu_keyboards.menu_main(),
        )

    @log_decorator(print_args=False, print_kwargs=False)
    async def menu_main(self, callback):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message="<b>Меню администратора</b>",
            keyboard=await self.admin_menu_keyboards.menu_main(),
        )
