from application.services.translation_service import TranslationService
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


class CanteensKeyboardsBuilder:
    def __init__(self, translation_service: TranslationService):
        self.translation_service = translation_service

    def get_canteens(self, locale: str):
        canteens = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Mensa Erlenring",
                                         callback_data="canteen_mensa_erlenring"),

                    InlineKeyboardButton(text="Mensa Lahnberge",
                                         callback_data="canteen_mensa_lahnberge")
                ],

                [
                    InlineKeyboardButton(text="Bistro",
                                         callback_data="canteen_bistro"),
                    InlineKeyboardButton(text="THM",
                                         callback_data="canteen_thm")
                ],

                [
                    InlineKeyboardButton(text="Cafeteria Lahnberge",
                                         callback_data="canteen_cafeteria_lahnberge"),

                    InlineKeyboardButton(text="Mo's Diner",
                                         callback_data="canteen_mo_diner"),

                    InlineKeyboardButton(text="Colibri",
                                         callback_data="canteen_colibri")
                ],

                [
                    InlineKeyboardButton(
                        text=self.translation_service.translate(message_id='to-menu-main', locale=locale),
                        callback_data="menu_main")
                ],
            ]
        )
        return canteens
