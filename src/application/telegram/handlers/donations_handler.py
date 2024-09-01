from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery

from application.services.translation_service import TranslationService
from application.telegram.keyboards.navigator_keyboards import NavigatorKeyboardsBuilder


class DonationsHandler:
    def __init__(self, translation_service: TranslationService, navigator_keyboards: NavigatorKeyboardsBuilder):
        self.translation_service = translation_service
        self.navigator_keyboards = navigator_keyboards

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        pass

    def __register_callbacks(self, router: Router):
        router.callback_query.register(self.menu_donations, F.data == "menu_donations")

    async def menu_donations(self, call: CallbackQuery, locale: str = 'ru'):
        await call.message.edit_text(
            await self.translation_service.translate(message_id='menu-donations', locale=locale),
            reply_markup=await self.navigator_keyboards.get_go_to_menu_main(locale=locale),
            parse_mode=ParseMode.MARKDOWN
        )
        # await call.answer()
