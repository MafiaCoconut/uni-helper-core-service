from application.services.translation_service import TranslationService
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from application.telegram.keyboards.navigator_keyboards import NavigatorKeyboardsBuilder
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from application.telegram.keyboards.translation_keyboards import TranslationKeyboardsBuilder


class AuthorizationKeyboardsBuilder:
    def __init__(self,
                 translation_service: TranslationService,
                 settings_keyboards: SettingsKeyboardsBuilder,
                 navigator_keyboards: NavigatorKeyboardsBuilder,
                 translation_keyboards: TranslationKeyboardsBuilder,
                 ):
        self.translation_service = translation_service
        self.settings_keyboards = settings_keyboards
        self.navigator_keyboards = navigator_keyboards
        self.translation_keyboards = translation_keyboards

    async def get_languages_list_from_start(self, locale: str):
        languages = await self.translation_keyboards.get_locales_list('authorization_locales_config')

        languages.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='to-change-canteen', locale=locale),
                    callback_data='change_canteen start')
            ]
        )

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
                        callback_data="authorization_canteen_set -")
                ]

            ]
        )
        return change_canteen

    async def send_main_menu(self, locale: str):
        return await self.navigator_keyboards.get_send_menu_main(locale=locale)
