from application.interfaces.telegram_interface import TelegramInterface
from application.services.translation_service import TranslationService
from application.services.users_service import UsersService
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from domain.entities.user import User


class SettingsUseCase:
    def __init__(self,
                 users_service: UsersService,
                 translation_service: TranslationService,
                 telegram_interface: TelegramInterface,
                 settings_keyboards: SettingsKeyboardsBuilder
                 ):
        self.users_service = users_service
        self.translation_service = translation_service
        self.telegram_interface = telegram_interface
        self.settings_keyboards = settings_keyboards

    async def get_settings_text(self, user_id: int, locale: str):
        user = await self.users_service.get_user(user_id=user_id)

        text = await self.translation_service.translate(message_id='menu-settings-heading', locale=locale) + '\n'
        if user.canteen_id == 0:
            text += await self.translation_service.translate(message_id='menu-settings-mailing-on', locale=locale) + '\n'
            text += await self.translation_service.translate(message_id='menu-settings-mailing-time', locale=locale,
                                                             mailing_time=user.mailing_time) + '\n'
            text += await self.translation_service.translate(message_id='menu-settings-canteen', locale=locale) + '\n'
        else:
            text += await self.translation_service.translate(message_id='menu-settings-mailing-off', locale=locale) +'\n'

        text += '\n' + await self.translation_service.translate(message_id='menu-settings-ending', locale=locale)

        return text

    async def menu_settings(self, callback, user_id: int, locale: str):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message=await self.get_settings_text(user_id=user_id, locale=locale),
            keyboard=await self.settings_keyboards.get_menu(locale=locale),
        )



