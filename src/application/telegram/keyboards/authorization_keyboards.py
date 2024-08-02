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
                    callback_data='authorization_canteens_config')
            ]
        )

        return languages

    async def get_canteens_list_to_change(self, locale: str):
        change_canteen = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Mensa Erlenring",
                                         callback_data="authorization_canteen_set_check 1"),
                    InlineKeyboardButton(text="Mensa Lahnberge",
                                         callback_data="authorization_canteen_set_check 2")
                ],
                [
                    InlineKeyboardButton(text="Bistro", callback_data="authorization_canteen_set_check 3"),
                    InlineKeyboardButton(text="THM", callback_data="authorization_canteen_set_check 6")
                ],
                [
                    InlineKeyboardButton(
                        text=await self.translation_service.translate(
                            message_id='disable-mailing-canteen',
                            locale=locale
                        ),
                        callback_data="authorization_canteen_set_check 0")
                ]

            ]
        )
        return change_canteen

    async def send_main_menu(self, locale: str):
        return await self.navigator_keyboards.get_send_menu_main(locale=locale)

    async def get_check_status_change_canteen(self, canteen_id: str, locale: str):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=await self.translation_service.translate(message_id='save', locale=locale),
                        callback_data=f'authorization_canteen_set {canteen_id}')
                ],
                [
                    InlineKeyboardButton(
                        text=await self.translation_service.translate(message_id='change', locale=locale),
                        callback_data='authorization_canteens_config')
                ]
            ]
        )
        return keyboard
