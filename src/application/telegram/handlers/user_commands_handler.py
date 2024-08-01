from application.services.translation_service import TranslationService

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from application.telegram.keyboards.menu_main_keyboards import MenuMainKeyboardsBuilder
from application.telegram.keyboards.navigator_keyboards import NavigatorKeyboardsBuilder


class UserCommandsHandler:
    def __init__(self, translation_service: TranslationService, menu_main_keyboards: MenuMainKeyboardsBuilder):
        self.translation_service = translation_service
        self.menu_main_keyboards = menu_main_keyboards

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        return router

    def __register_handlers(self, router: Router):
        # router.message(CommandStart())(self.command_start_handler)
        router.message(Command("main_menu"))(self.command_main_menu_handler)

    async def command_main_menu_handler(self, message: Message, state: FSMContext, locale: str = 'ru') -> None:
        if not await state.get_data():
            await message.answer(
                await self.translation_service.translate('menu-main', locale=locale),
                reply_markup=await self.menu_main_keyboards.get_menu_main(locale=locale)
            )


