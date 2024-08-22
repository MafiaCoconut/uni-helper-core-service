from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from application.services.admin_service import AdminsService
from application.telegram.filters.is_admin import IsAdmin


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

    def __register_callbacks(self, router: Router):
        router.callback_query.register(self.menu_admin_main_callback, F.data.startswith("admin_menu_help"))
        router.callback_query.register(self.menu_users, F.data.startswith("admin_menu_users"))
        router.callback_query.register(self.menu_canteens, F.data.startswith("admin_menu_canteens"))
        router.callback_query.register(self.menu_stadburo, F.data.startswith("admin_menu_stadburo"))
        router.callback_query.register(self.menu_logs, F.data.startswith("admin_menu_logs"))

        router.callback_query.register(self.get_all_users_data, F.data.startswith("admin_get_all_users"))

    async def menu_admin_main_handler(self, message: Message):
        await self.admins_service.send_menu_admin_main(user_id=message.chat.id)

    async def menu_admin_main_callback(self, message: Message):
        await self.admins_service.send_menu_admin_main(user_id=message.chat.id)

    async def menu_users(self, callback: CallbackQuery):
        await self.admins_service.menu_users(callback=callback)

    async def get_all_users_data(self, callback: CallbackQuery):
        await self.admins_service.get_all_users_data(callback=callback)

    async def menu_canteens(self, callback: CallbackQuery):
        await self.admins_service.menu_canteens(callback=callback)

    async def menu_stadburo(self, callback: CallbackQuery):
        await self.admins_service.menu_stadburo(callback=callback)

    async def menu_logs(self, callback: CallbackQuery):
        await self.admins_service.menu_logs(callback=callback)

