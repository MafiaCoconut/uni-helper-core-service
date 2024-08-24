from aiohttp.log import web_logger

from application.gateways.users_gateway import UsersGateway
from application.interfaces.telegram_interface import TelegramInterface
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder


class AdminMenuLogsUseCase:
    def __init__(self,
                 # users_gateway: UsersGateway,
                 telegram_interface: TelegramInterface,
                 admin_menu_keyboards: AdminMenuKeyboardsBuilder,
                 ):
        # self.users_gateway = users_gateway
        self.telegram_interface = telegram_interface
        self.admin_menu_keyboards = admin_menu_keyboards
        self.system_logs_path = "logs/system_data.log"
        self.user_logs_path = "logs/user_data.log"
        self.error_logs_path = "logs/error_data.log"

    async def menu(self, callback):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message="<b>Меню работы с пользователями</b>",
            keyboard=await self.admin_menu_keyboards.menu_logs(),
        )

    async def send_logs(self, callback):
        user_id = callback.message.chat.id
        await self.telegram_interface.send_file(chat_id=user_id, file_path=self.system_logs_path)
        await self.telegram_interface.send_file(chat_id=user_id, file_path=self.user_logs_path)
        await self.telegram_interface.send_file(chat_id=user_id, file_path=self.error_logs_path)

        try:
            await self.telegram_interface.edit_message_with_callback(
                callback=callback,
                message="<b>Меню работы с логами</b>\n\n Логи отправлены",
                keyboard=await self.admin_menu_keyboards.menu_logs(),
            )
        except:
            pass

    async def clear_logs(self, callback):
        with open(self.system_logs_path, "w") as file:
            file.write(" ")
        with open(self.user_logs_path, "w") as file:
            file.write(" ")
        with open(self.error_logs_path, "w") as file:
            file.write(" ")

        try:
            await self.telegram_interface.edit_message_with_callback(
                callback=callback,
                message="<b>Меню работы с логами</b>\n\n Логи очищены",
                keyboard=await self.admin_menu_keyboards.menu_logs(),
            )
        except:
            pass
