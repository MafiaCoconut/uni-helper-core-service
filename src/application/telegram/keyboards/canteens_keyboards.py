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
                                         callback_data="canteen_menu 1"),

                    InlineKeyboardButton(text="Mensa Lahnberge",
                                         callback_data="canteen_menu 2")
                ],

                [
                    InlineKeyboardButton(text="Bistro",
                                         callback_data="canteen_menu 3"),
                    InlineKeyboardButton(text="Cafeteria Lahnberge",
                                         callback_data="canteen_menu 4"),
                ],

                [
                    InlineKeyboardButton(text="THM",
                                         callback_data="canteen_menu 6")

                    # InlineKeyboardButton(text="Mo's Diner",
                    #                      callback_data="canteen_menu 5"),

                    # InlineKeyboardButton(text="Colibri",
                    #                      callback_data="canteen_menu ")
                ],

                [
                    InlineKeyboardButton(
                        text=self.translation_service.translate(message_id='to-menu-main', locale=locale),
                        callback_data="menu_main")
                ],
            ]
        )
        return canteens
