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

    def get_languages_list_from_start(self, where_was_called: str, locale: str):
        languages = self.settings_keyboards.get_languages_list('from_start')

        languages.inline_keyboard.append([InlineKeyboardButton(
            text=self.translation_service.translate(message_id='to-change-canteen', locale=locale),
            callback_data=f'change_canteen {where_was_called}')])
        # menu_main = get_send_menu_main(l10n)
        # languages.inline_keyboard.append(menu_main.inline_keyboard[0])

        return languages
