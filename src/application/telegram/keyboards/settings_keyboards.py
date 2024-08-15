from application.services.translation_service import TranslationService
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from application.telegram.keyboards.navigator_keyboards import NavigatorKeyboardsBuilder
from application.telegram.keyboards.translation_keyboards import TranslationKeyboardsBuilder


class SettingsKeyboardsBuilder:
    def __init__(self,
                 translation_service: TranslationService,
                 translation_keyboards: TranslationKeyboardsBuilder,
                 navigator_keyboards: NavigatorKeyboardsBuilder,

                 ):
        self.translation_service = translation_service
        self.translation_keyboards = translation_keyboards
        self.navigator_keyboards = navigator_keyboards

    async def get_languages_list(self):
        languages = await self.translation_keyboards.get_locales_list(where_was_called='settings_locales_config')
        return languages

    async def get_menu(self, locale: str) -> InlineKeyboardMarkup:
        languages = await self.get_languages_list()

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [languages.inline_keyboard[0][i] for i in range(len(languages.inline_keyboard[0]))],

                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='change-mailing-time', locale=locale),
                    callback_data="settings_change_mailing_time")],

                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='change-status-mailing', locale=locale),
                    callback_data="change_status_mailing")],

                # [InlineKeyboardButton(text=l10n.format_value('change-status-numbers-in-menu'),
                #                       callback_data="change_status_numbers_in_menu")],

                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='change-canteen', locale=locale),
                    callback_data='change_canteen_from_settings')],

                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='to-menu-main', locale=locale),
                    callback_data="menu_main")],
            ]
        )
        return keyboard

    async def get_canteens_list_to_change(self, locale: str) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Mensa Erlenring",
                                         callback_data="settings_canteen_change mensa_erlenring"),
                    InlineKeyboardButton(text="Mensa Lahnberge",
                                         callback_data="settings_canteen_change mensa_lahnberge")
                ],
                [
                    InlineKeyboardButton(text="Bistro", callback_data="settings_canteen_change bistro"),
                    InlineKeyboardButton(text="THM", callback_data="settings_canteen_change thm")
                ],
                [
                    InlineKeyboardButton(
                        text=await self.translation_service.translate(message_id='disable-mailing-canteen', locale=locale),
                        callback_data="settings_canteen_change -")]

            ]
        )
        return keyboard

    async def get_check_status_change_canteen(self, locale: str, canteen_name: str):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=await self.translation_service.translate(message_id='save', locale=locale),
                                      callback_data=f'settings_canteen_yes {canteen_name}')],
                [InlineKeyboardButton(text=await self.translation_service.translate(message_id='change', locale=locale),
                                      callback_data='change_canteen from_settings')]
            ]
        )
        return keyboard

    async def get_change_mailing_time(self, locale: str):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="11:30", callback_data="settings_change_mailing_time 10:00"),
                    InlineKeyboardButton(text="12:00", callback_data="settings_change_mailing_time 11:00")
                ],
                [
                    InlineKeyboardButton(text="12:30", callback_data="settings_change_mailing_time 12:00"),
                    InlineKeyboardButton(text="13:00", callback_data="settings_change_mailing_time 13:00")
                ]
            ]
        )
        keyboard_go_to_menu_settings = await self.navigator_keyboards.get_go_to(locale=locale, where="settings")
        keyboard.inline_keyboard.append(keyboard_go_to_menu_settings.inline_keyboard[0])

        return keyboard
