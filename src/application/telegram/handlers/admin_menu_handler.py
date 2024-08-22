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
        router.callback_query.register(self.menu_users, F.data.startswith("admin_menu_users"))
        router.callback_query.register(self.menu_canteens, F.data.startswith("admin_menu_canteens"))
        router.callback_query.register(self.menu_stadburo, F.data.startswith("admin_menu_stadburo"))
        router.callback_query.register(self.menu_logs, F.data.startswith("admin_menu_logs"))

    async def menu_admin_main_handler(self, message: Message):
        await self.admins_service.send_menu_admin_main(user_id=message.chat.id)

    async def menu_users(self, callback: CallbackQuery):
        pass

    async def menu_canteens(self, callback: CallbackQuery):
        pass

    async def menu_stadburo(self, callback: CallbackQuery):
        pass

    async def menu_logs(self, callback: CallbackQuery):
        pass