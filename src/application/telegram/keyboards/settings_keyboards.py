from application.services.translation_service import TranslationService
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from application.telegram.keyboards.translation_keyboards import TranslationKeyboardsBuilder


class SettingsKeyboardsBuilder:
    def __init__(self,
                 translation_service: TranslationService,
                 translation_keyboards: TranslationKeyboardsBuilder,
                 ):
        self.translation_service = translation_service
        self.translation_keyboards = translation_keyboards

    async def get_languages_list(self, locale: str):
        languages = await self.translation_keyboards.get_locales_list(where_was_called='settings_locales_config')

        # languages.inline_keyboard.append(
        #     [
        #         InlineKeyboardButton(
        #             text=await self.translation_service.translate(message_id='to-change-canteen', locale=locale),
        #             callback_data='settings_canteens_config')
        #     ]
        # )

        return languages

    async def get_menu(self, locale: str) -> InlineKeyboardMarkup:
        languages = await self.get_languages_list(locale=locale)

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [languages.inline_keyboard[0][i] for i in range(len(languages.inline_keyboard[0]))],

                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='change-mailing-time', locale=locale),
                    callback_data="change_mailing_time")],

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

    def get_canteens_list_to_change(self, locale: str) -> InlineKeyboardMarkup:
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
                        text=self.translation_service.translate(message_id='disable-mailing-canteen', locale=locale),
                        callback_data="settings_canteen_change -")]

            ]
        )
        return keyboard

    def get_check_status_change_canteen(self, locale: str, canteen_name: str):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=self.translation_service.translate(message_id='save', locale=locale),
                                      callback_data=f'settings_canteen_yes {canteen_name}')],
                [InlineKeyboardButton(text=self.translation_service.translate(message_id='change', locale=locale),
                                      callback_data='change_canteen from_settings')]
            ]
        )
        return keyboard
