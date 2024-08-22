from aiogram import Router, F
from aiogram.types import Message, CallbackQuery


from application.telegram.filters.is_admin import IsAdmin


class AdminMenuHandler:
    def __init__(self,
                 ):
        pass

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        router.message(F.text == "/help_a", IsAdmin())(self.menu_admin_main_handler)

    def __register_callbacks(self, router: Router):
        pass

    async def menu_admin_main_handler(self, message: Message):
        await message.answer("", reply_markup=)
