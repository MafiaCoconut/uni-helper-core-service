import logging

from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from icecream import ic

from application.services.canteens_service import CanteensService
from application.services.translation_service import TranslationService
from application.telegram.keyboards.canteens_keyboards import CanteensKeyboardsBuilder
from infrastructure.config.logs_config import log_decorator


class CanteensHandler:
    def __init__(self,
                 translation_service: TranslationService,
                 canteens_keyboards: CanteensKeyboardsBuilder,
                 canteens_service: CanteensService
                 ):
        self.translation_service = translation_service
        self.canteens_keyboards = canteens_keyboards
        self.canteens_service = canteens_service

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        pass

    def __register_callbacks(self, router: Router):
        router.callback_query.register(self.menu_canteens_handler, F.data == "menu_canteens")
        router.callback_query.register(self.canteens_handler, F.data.startswith('canteen'))

    async def menu_canteens_handler(self, call: CallbackQuery, locale: str = 'ru'):
        """
        Меню выбора столовой для получения меню этой столовой
        :param call: Объект CallbackQuery
        :param locale:
        """
        await call.message.edit_text(
            await self.translation_service.translate(message_id='menu-canteens', locale=locale),
            reply_markup=await self.canteens_keyboards.get_canteens(locale=locale)
        )

    async def canteens_handler(self, call: CallbackQuery, locale: str = 'ru'):
        """
        Вывод информацию о меню конкретной столовой
        :param call: Объект CallbackQuery
        :param locale: Языковая локаль
        """
        canteen_id = call.data[call.data.find(' ')+1:]
        ic(canteen_id)

        canteen_menu = await self.canteens_service.get_canteens_menu(canteen_id=canteen_id, locale=locale)

        try:
            await call.message.edit_text(
                text=canteen_menu,
                reply_markup=await self.canteens_keyboards.get_canteens(locale=locale))
        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error('The text canteens menu has not changed')
            error_logger.error(e)

        await call.answer()
