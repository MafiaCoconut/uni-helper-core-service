import logging

from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from icecream import ic

from application.services.translation_service import TranslationService
from application.telegram.keyboards.links_keyboards import LinksKeyboardsBuilder


class LinksHandler:
    def __init__(self,
                 translation_service: TranslationService,
                 links_keyboards: LinksKeyboardsBuilder,
                 ):
        self.translation_service = translation_service
        self.links_keyboards = links_keyboards

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        pass

    def __register_callbacks(self, router: Router):
        router.callback_query.register(self.menu_links_first_page, F.data == 'menu_links')
        router.callback_query.register(self.menu_links_first_page, F.data == 'menu_links_first_page')
        router.callback_query.register(self.menu_links_second_page, F.data == 'menu_links_second_page')

    async def menu_links_first_page(self, call: CallbackQuery, locale: str = 'ru'):
        await call.message.edit_text(
            text=await self.translation_service.translate(message_id='menu-links', locale=locale),
            reply_markup=await self.links_keyboards.get_first_page_links(locale=locale))
        await call.answer()

    async def menu_links_second_page(self, call: CallbackQuery, locale: str = 'ru'):
        await call.message.edit_text(
            text=await self.translation_service.translate(message_id='menu-links', locale=locale),
            reply_markup=await self.links_keyboards.get_second_page_links(locale=locale))
        await call.answer()

    # async def show_main_links_handler(self, call: CallbackQuery, locale: str = 'ru'):
    #     await call.message.edit_reply_markup(reply_markup=inline.get_main_links(l10n))
    #     await call.answer()
