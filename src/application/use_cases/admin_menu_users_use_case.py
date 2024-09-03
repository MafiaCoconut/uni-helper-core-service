from icecream import ic
from datetime import datetime

from application.gateways.users_gateway import UsersGateway
from application.interfaces.excel_interface import ExcelInterface
from application.interfaces.telegram_interface import TelegramInterface
from application.services.users_service import UsersService
from application.telegram.keyboards.admin_keyboards import AdminKeyboardsBuilder
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder
from application.telegram.models.states import GetPersonById
from infrastructure.config.logs_config import log_decorator


class AdminMenuUsersUseCase:
    def __init__(self,
                 users_service: UsersService,
                 telegram_interface: TelegramInterface,
                 excel_interface: ExcelInterface,
                 admin_keyboards: AdminKeyboardsBuilder,
                 admin_menu_keyboards: AdminMenuKeyboardsBuilder,
                 ):
        self.users_service = users_service
        self.telegram_interface = telegram_interface
        self.excel_interface = excel_interface
        self.admin_keyboards = admin_keyboards
        self.admin_menu_keyboards = admin_menu_keyboards

        self.path_to_tmp_file = "data/users.xlsx"

    @log_decorator(print_args=False, print_kwargs=False)
    async def menu(self, callback):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message="<b>Меню работы с пользователями</b>",
            keyboard=await self.admin_menu_keyboards.menu_users(),
        )

    @log_decorator(print_args=False, print_kwargs=False)
    async def get_all_users_data_in_xslx(self, callback):
        users = await self.users_service.get_users()
        headers = list(users[0].model_fields.keys())

        rows = []
        for user in users:
            rows.append([getattr(user, field) for field in headers[:-2]])
            rows[-1].append(await self.refactor_created_datetime(getattr(user, headers[-2])))
            rows[-1].append(await self.refactor_created_datetime(getattr(user, headers[-1])))

        await self.excel_interface.save_to_excel(headers=headers, rows=rows, path=self.path_to_tmp_file)

        await self.telegram_interface.send_file(chat_id=callback.message.chat.id, file_path=self.path_to_tmp_file)
        await callback.answer()

        await self.excel_interface.clear(path=self.path_to_tmp_file)

    @log_decorator(print_args=False, print_kwargs=False)
    async def refactor_created_datetime(self, data: datetime):
        time = f"{str(data.hour).zfill(2)}:{str(data.minute).zfill(2)}"
        day = f"{str(data.day).zfill(2)}.{str(data.month).zfill(2)}.{str(data.year).zfill(2)}"
        return f"{time} - {day}"

    @log_decorator(print_args=False, print_kwargs=False)
    async def get_count_users(self, callback):
        users = await self.users_service.get_users()
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message=f"<b>Количество пользователей: {len(users)}</b>",
            keyboard=await self.admin_menu_keyboards.menu_users(),
        )

    @log_decorator(print_args=False, print_kwargs=False)
    async def request_to_user_data(self, callback, state):
        callback_message = await callback.message.edit_text(
            text="Введи id пользователя, ссылку на которого хочешь получить",
            reply_markup=await self.admin_keyboards.go_to('users'))

        await state.update_data(last_admin_menu_message=callback_message.message_id)
        await state.set_state(GetPersonById.last_help_message_id)

    @log_decorator(print_args=False, print_kwargs=False)
    async def get_user_data(self, message, state, user_id):
        data = await state.get_data()
        last_admin_menu_message = data.get('last_admin_menu_message')

        user = await self.users_service.get_user(user_id=user_id)

        text = ("Информация о пользователе\n\n"
                f"ID: {user.user_id}\n"
                f"Username: @{user.username}\n"
                f"Name: {user.name}\n"
                f"Locale: {user.locale}\n\n"
                f"Mailing time: {user.mailing_time}\n"
                f"CanteenID: {user.canteen_id}\n\n"
                f"Created time: {user.created_at}")

        await self.telegram_interface.edit_message(
            chat_id=message.chat.id,
            message_id=last_admin_menu_message,
            message=text,
            keyboard=await self.admin_keyboards.get_link_to_person(user_id=user_id)
        )

        await state.set_state(None)
