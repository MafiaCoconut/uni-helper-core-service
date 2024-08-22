from icecream import ic
from datetime import datetime

from application.gateways.users_gateway import UsersGateway
from application.interfaces.excel_interface import ExcelInterface
from application.interfaces.telegram_interface import TelegramInterface
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder


class AdminMenuUsersUseCase:
    def __init__(self,
                 users_gateway: UsersGateway,
                 telegram_interface: TelegramInterface,
                 excel_interface: ExcelInterface,
                 admin_menu_keyboards: AdminMenuKeyboardsBuilder,
                 ):
        self.users_gateway = users_gateway
        self.telegram_interface = telegram_interface
        self.excel_interface = excel_interface
        self.admin_menu_keyboards = admin_menu_keyboards

    async def menu(self, callback):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message="<b>Меню работы с пользователями</b>",
            keyboard=await self.admin_menu_keyboards.menu_users(),
        )

    async def get_all_users_data_in_xslx(self, callback):
        users = await self.users_gateway.get_users_all()
        headers = list(users[0].model_fields.keys())

        ic(headers)
        rows = []
        for user in users:
            rows.append([getattr(user, field) for field in headers[:-2]])
            rows[-1].append(self.refactor_created_datetime(getattr(user, headers[-2])))
            rows[-1].append(self.refactor_created_datetime(getattr(user, headers[-1])))

        ic(rows)

        await self.excel_interface.save_to_excel(headers=headers, rows=rows, path="data/users.xlsx")

        await self.telegram_interface.send_file(chat_id=callback.message.chat.id, file_path="data/users.xlsx")

        await self.excel_interface.clear(path="data/users.xlsx")
        """
        получить данные о пользователях
        преобразовать их
        отправить
               :return:
        """

    def refactor_created_datetime(self, data: datetime):
        time = f"{str(data.hour).zfill(2)}:{str(data.minute).zfill(2)}"
        day = f"{str(data.day).zfill(2)}.{str(data.month).zfill(2)}.{str(data.year).zfill(2)}"
        return f"{time} - {day}"
