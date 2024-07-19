from application.services.translation_service import TranslationService
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


class StadburoKeyboardsBuilder:
    def __init__(self, translation_service: TranslationService):
        self.translation_service = translation_service

    def get_menu_stadburo(self, locale: str) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(
                    text="Ausländerbehörde / Immigration Office",
                    callback_data="menu_immigration")],

                [InlineKeyboardButton(
                    text="Stadtbüro / Registration Office",
                    callback_data="registration")],

                [InlineKeyboardButton(
                    text="Others",
                    callback_data="stadtburo_others")],

                [InlineKeyboardButton(
                    text=self.translation_service.translate(message_id='to-menu-main', locale=locale),
                    callback_data="menu_main")],
            ]
        )
        return keyboard

    def get_menu_immigration_officec(self, locale: str) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                # [InlineKeyboardButton(text="Aufenthaltstitel beantragen",
                #                       callback_data="aufenthaltstitel")],
                [InlineKeyboardButton(text="Adressänderung",
                                      callback_data="adressanderung")],
                [InlineKeyboardButton(text="eAT-Abholung",
                                      callback_data="eat_abholung")],

                [InlineKeyboardButton(text=self.translation_service.translate(message_id='back', locale=locale),
                                      callback_data="menu_stadburo"),
                 InlineKeyboardButton(text=self.translation_service.translate(message_id='to-menu-main', locale=locale),
                                      callback_data="menu_main")],
            ]
        )
        return keyboard
