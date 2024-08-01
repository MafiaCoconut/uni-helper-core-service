from application.services.translation_service import TranslationService
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder


class AuthorizationKeyboardsBuilder:
    def __init__(self,
                 translation_service: TranslationService,
                 settings_keyboards: SettingsKeyboardsBuilder,
                 ):
        self.translation_service = translation_service
        self.settings_keyboards = settings_keyboards

    async def get_languages_list_from_start(self, locale: str):
        languages = self.settings_keyboards.get_languages_list('from_start')

        languages.inline_keyboard.append([InlineKeyboardButton(
            text=await self.translation_service.translate(message_id='to-change-canteen', locale=locale),
            callback_data='change_canteen start')])
        # menu_main = get_send_menu_main(l10n)
        # languages.inline_keyboard.append(menu_main.inline_keyboard[0])

        return languages

    async def get_canteens_list_to_change(self, locale: str):
        change_canteen = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Mensa Erlenring",
                                         callback_data="authorization_canteen_set mensa_erlenring"),
                    InlineKeyboardButton(text="Mensa Lahnberge",
                                         callback_data="authorization_canteen_set mensa_lahnberge")
                ],
                [
                    InlineKeyboardButton(text="Bistro", callback_data="authorization_canteen_set bistro"),
                    InlineKeyboardButton(text="THM", callback_data="authorization_canteen_set thm")
                ],
                [
                    InlineKeyboardButton(
                        text=await self.translation_service.translate(
                            message_id='disable-mailing-canteen',
                            locale=locale
                        ),
                        callback_data="settings_canteen_change -")
                ]

            ]
        )
        return change_canteen
