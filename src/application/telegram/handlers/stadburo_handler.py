import logging

from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from icecream import ic

from application.services.translation_service import TranslationService
from application.services.stadburo_service import StadburoService
from application.telegram.keyboards.navigator_keyboards import NavigatorKeyboardsBuilder
from application.telegram.keyboards.stadburo_keyboards import StadburoKeyboardsBuilder


class StadburoHandler:
    def __init__(self,
                 translation_service: TranslationService,
                 stadburo_service: StadburoService,
                 stadburo_keyboards: StadburoKeyboardsBuilder,
                 navigator_keyboards: NavigatorKeyboardsBuilder,
                 ):
        self.translation_service = translation_service
        self.stadburo_service = stadburo_service
        self.stadburo_keyboards = stadburo_keyboards
        self.navigator_keyboards = navigator_keyboards

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        pass

    def __register_callbacks(self, router: Router):
        router.callback_query.register(self.menu_stadburo_handler, F.data.startswith('menu_stadburo'))
        router.callback_query.register(self.menu_immigration_handler, F.data.startswith('menu_immigration'))
        router.callback_query.register(self.category_of_termins_handler, F.data.startswith('category_of_termins'))

    async def menu_stadburo_handler(self, call: CallbackQuery, locale: str = 'ru'):
        await call.message.edit_text(
            self.translation_service.translate(message_id='menu-stadburo', locale=locale),
            reply_markup=self.stadburo_keyboards.get_menu_stadburo(locale=locale))
        await call.answer()

    async def menu_immigration_handler(self, call: CallbackQuery, locale: str = 'ru'):
        await call.message.edit_text(
            self.translation_service.translate(message_id='menu-immigration', locale=locale),
            reply_markup=self.stadburo_keyboards.get_menu_immigration_office(locale=locale))
        await call.answer()

    async def category_of_termins_handler(self, call: CallbackQuery, locale: str = 'ru'):
        category_id = call.data[call.data.find(' ') + 1:]

        text = await self.stadburo_service.get_termins_text(category_id=category_id, locale=locale)
        await call.message.edit_text(
            text=text,
            reply_markup=self.navigator_keyboards.get_go_to(locale=locale, where='stadburo')
        )
        await call.answer()


    # async def adressanderung_handler(self, call: CallbackQuery, locale: str = 'ru'):
    #     await call.message.edit_text(
    #         await self.stadburo_service.get_termins_text(category_id=1, locale=locale),
    #         reply_markup=self.navigator_keyboards.get_go_to(locale=locale, where='stadburo'))
    #
    # async def eat_abholung_handler(self, call: CallbackQuery, locale: str = 'ru'):
    #     await call.message.edit_text(
    #         await self.stadburo_service.get_termins_text(category_id=2, locale=locale),
    #         reply_markup=self.navigator_keyboards.get_go_to(locale=locale, where='stadburo'))
    #
    # async def registration_office_handler(self, call: CallbackQuery, locale: str = 'ru'):
    #     await call.message.edit_text(
    #         await self.stadburo_service.get_termins_text(category_id=3, locale=locale),
    #         reply_markup=self.navigator_keyboards.get_go_to(locale=locale, where='stadburo')
    #     )
    #
    # async def stadtburo_others_handler(self, call: CallbackQuery, locale: str = 'ru'):
    #     await call.message.edit_text(
    #         await self.stadburo_service.get_termins_text(category_id=4, locale=locale),
    #         reply_markup=self.navigator_keyboards.get_go_to(locale=locale, where='stadburo'))

    # async def send_termins(self, call: CallbackQuery, data, locale: str = 'ru'):
    #     """Функция отправки списка терминов"""
    #
    #     if len(data) <= 50:
    #         await call.message.edit_text(self.translation_service.translate(message_id='lack-of-terms'),
    #                                      reply_markup=inline.get_go_to(l10n, 'immigration'))
    #     else:
    #         await call.message.edit_text(data, reply_markup=inline.get_go_to(l10n, 'immigration'))
