from icecream import ic

from application.interfaces.telegram_interface import TelegramInterface
from application.services.canteens_service import CanteensService
from application.services.translation_service import TranslationService
from application.services.users_service import UsersService
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from application.use_cases.settings_user_data_use_case import SettingsUserDataUseCase
from domain.entities.user import User
from infrastructure.config.logs_config import log_decorator


class SettingsUseCase:
    def __init__(self,
                 users_service: UsersService,
                 translation_service: TranslationService,
                 canteens_service: CanteensService,
                 telegram_interface: TelegramInterface,
                 settings_keyboards: SettingsKeyboardsBuilder,
                 update_user_data_use_case: SettingsUserDataUseCase,
                 ):
        self.users_service = users_service
        self.translation_service = translation_service
        self.canteens_service = canteens_service
        self.telegram_interface = telegram_interface
        self.settings_keyboards = settings_keyboards
        self.update_user_data_use_case = update_user_data_use_case

    async def get_settings_text(self, user_id: int, locale: str):
        user = await self.users_service.get_user(user_id=user_id)
        ic(user)
        text = await self.translation_service.translate(message_id='menu-settings-heading', locale=locale) + '\n'
        if user.canteen_id != 0:
            text += await self.translation_service.translate(message_id='menu-settings-mailing-on', locale=locale) + '\n'
            text += await self.translation_service.translate(message_id='menu-settings-mailing-time', locale=locale,
                                                             mailing_time=user.mailing_time) + '\n'
            canteen = await self.canteens_service.get_canteens_info(canteen_id=user.canteen_id)
            text += await self.translation_service.translate(
                message_id='menu-settings-canteen', locale=locale,
                canteen=canteen.name + '\n'
            )
        else:
            text += await self.translation_service.translate(message_id='menu-settings-mailing-off', locale=locale) + '\n'

        text += '\n' + await self.translation_service.translate(message_id='menu-settings-ending', locale=locale)

        return text

    @log_decorator
    async def menu_settings(self, callback, user_id: int, locale: str):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message=await self.get_settings_text(user_id=user_id, locale=locale),
            keyboard=await self.settings_keyboards.get_menu(locale=locale),
        )

    @log_decorator
    async def change_locale(self, callback, user_id: int, new_locale: str):
        await self.update_user_data_use_case.update_locale(user_id=user_id, new_locale=new_locale)
        try:
            await self.telegram_interface.edit_message_with_callback(
                callback=callback,
                message=await self.get_settings_text(user_id=user_id, locale=new_locale),
                keyboard=await self.settings_keyboards.get_menu(locale=new_locale),
            )
        except Exception as e:
            ic(e)


