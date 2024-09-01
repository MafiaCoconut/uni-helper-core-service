from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery, Message

from application.services.translation_service import TranslationService
from application.telegram.keyboards.menu_main_keyboards import MenuMainKeyboardsBuilder


class MenuMainHandler:
    def __init__(self, translation_service: TranslationService, menu_main_keyboards: MenuMainKeyboardsBuilder):
        self.translation_service = translation_service
        self.menu_main_keyboards = menu_main_keyboards

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        pass

    def __register_callbacks(self, router: Router):
        router.callback_query.register(self.menu_main_handler, F.data == "menu_main")
        router.callback_query.register(self.menu_main_handler, F.data == "send_menu_main")

    async def menu_main_handler(self, call: CallbackQuery, locale: str = 'ru'):
        await call.message.edit_text(
            await self.translation_service.translate(message_id='menu-main', locale=locale),
            reply_markup=await self.menu_main_keyboards.get_menu_main(locale=locale),
            parse_mode=ParseMode.HTML
        )
        await call.answer()

    async def send_menu_main_handler(self, call: CallbackQuery, locale: str = 'ru'):
        await call.message.answer(
            await self.translation_service.translate(message_id='menu-main', locale=locale),
            reply_markup=await self.menu_main_keyboards.get_menu_main(locale=locale),
            parse_mode=ParseMode.HTML
        )



