from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from sqlalchemy.testing.suite.test_reflection import users

from application.services.admin_service import AdminsService
from application.telegram.filters.is_admin import IsAdmin
from application.telegram.models.states import GetPersonById


class AdminMenuHandler:
    def __init__(self,
                 admins_service: AdminsService,
                 ):
        self.admins_service = admins_service

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        router.message(F.text == "/help_a", IsAdmin())(self.menu_admin_main_handler)

        router.message(GetPersonById.last_help_message_id)(self.get_user_data_handler)

    def __register_callbacks(self, router: Router):
        router.callback_query.register(self.menu_admin_main_callback, F.data.startswith("admin_menu help"))
        router.callback_query.register(self.menu_users, F.data.startswith("admin_menu users"))
        router.callback_query.register(self.menu_canteens, F.data.startswith("admin_menu canteens"))
        router.callback_query.register(self.menu_stadburo, F.data.startswith("admin_menu stadburo"))
        router.callback_query.register(self.menu_logs, F.data.startswith("admin_menu logs"))

        router.callback_query.register(self.get_all_users_data, F.data.startswith("admin_get_all_users"))
        router.callback_query.register(self.get_count_users, F.data.startswith("admin_get_count_users"))
        router.callback_query.register(self.request_to_user_data, F.data.startswith("admin_get_person_by_id"))

        router.callback_query.register(self.parse_canteens_all, F.data == "admin_start_canteen_parser_all")
        router.callback_query.register(self.parse_canteen, F.data.startswith("admin_start_canteen_parser"))
        router.callback_query.register(self.get_canteen, F.data.startswith("admin_get_canteen"))
        # router.callback_query.register(self., F.data.startswith("admin_change_persons_parameters"))
        # router.callback_query.register(self., F.data.startswith("admin_delete_person"))

    async def menu_admin_main_handler(self, message: Message):
        await self.admins_service.send_menu_main(user_id=message.chat.id)

    async def menu_admin_main_callback(self, callback: CallbackQuery):
        await self.admins_service.menu_main(callback=callback)

    async def menu_users(self, callback: CallbackQuery):
        await self.admins_service.menu_users(callback=callback)

    async def get_all_users_data(self, callback: CallbackQuery):
        await self.admins_service.get_all_users_data(callback=callback)

    async def get_count_users(self, callback: CallbackQuery):
        await self.admins_service.get_count_users(callback=callback)

    async def request_to_user_data(self, callback: CallbackQuery, state: FSMContext):
        await self.admins_service.request_to_user_data(callback=callback, state=state)

    async def get_user_data_handler(self, message: Message, state: FSMContext):
        user_id = int(message.text)
        await self.admins_service.get_user_data(message=message, state=state, user_id=user_id)

    async def menu_canteens(self, callback: CallbackQuery):
        await self.admins_service.menu_canteens(callback=callback)

    async def parse_canteen(self, callback: CallbackQuery):
        canteen_id = int(callback.data[callback.data.find(' ') + 1:])
        await self.admins_service.parse_canteen(callback=callback, canteen_id=canteen_id)

    async def parse_canteens_all(self, callback: CallbackQuery):
        await self.admins_service.parse_canteen_all(callback=callback)

    async def get_canteen(self, callback: CallbackQuery):
        canteen_id = int(callback.data[callback.data.find(' ') + 1:])
        await self.admins_service.get_canteen(callback=callback, canteen_id=canteen_id)

    async def menu_stadburo(self, callback: CallbackQuery):
        await self.admins_service.menu_stadburo(callback=callback)

    async def menu_logs(self, callback: CallbackQuery):
        await self.admins_service.menu_logs(callback=callback)

