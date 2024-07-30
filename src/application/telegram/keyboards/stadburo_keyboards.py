from application.services.translation_service import TranslationService
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


class StadburoKeyboardsBuilder:
    def __init__(self, translation_service: TranslationService):
        self.translation_service = translation_service

    async def get_menu_stadburo(self, locale: str) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(
                    text="Ausländerbehörde / Immigration Office",
                    callback_data="menu_immigration")],

                [InlineKeyboardButton(
                    text="Stadtbüro / Registration Office",
                    callback_data="category_of_termins 3")],

                [InlineKeyboardButton(
                    text="Others",
                    callback_data="category_of_termins 4")],

                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='to-menu-main', locale=locale),
                    callback_data="menu_main")],
            ]
        )
        return keyboard

    async def get_menu_immigration_office(self, locale: str) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                # [InlineKeyboardButton(text="Aufenthaltstitel beantragen",
                #                       callback_data="aufenthaltstitel")],
                [InlineKeyboardButton(text="Adressänderung",
                                      callback_data="category_of_termins 1")],
                [InlineKeyboardButton(text="eAT-Abholung",
                                      callback_data="category_of_termins 2")],

                [
                    InlineKeyboardButton(
                        text=await self.translation_service.translate(message_id='back', locale=locale),
                        callback_data="menu_stadburo"),
                    InlineKeyboardButton(
                        text=await self.translation_service.translate(message_id='to-menu-main', locale=locale),
                        callback_data="menu_main")
                ],
            ]
        )
        return keyboard
