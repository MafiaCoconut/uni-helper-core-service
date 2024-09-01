from application.interfaces.telegram_interface import TelegramInterface
from application.services.canteens_service import CanteensService
from application.services.notification_service import NotificationService
from application.services.redis_service import RedisService
from application.services.users_service import UsersService
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from application.use_cases.settings_use_case import MenuSettingsUseCase
from application.use_cases.settings_user_data_use_case import SettingsUserDataUseCase
from domain.entities.user import User
from infrastructure.config.logs_config import log_decorator
from infrastructure.config.translation_config import translation_service


class SettingsService:
    def __init__(self,
                 users_service: UsersService,
                 redis_service: RedisService,
                 notification_service: NotificationService,
                 canteens_service: CanteensService,
                 telegram_interface: TelegramInterface,
                 settings_keyboards: SettingsKeyboardsBuilder,
                 ):
        self.settings_keyboards = settings_keyboards
        self.telegram_interface = telegram_interface
        self.settings_user_data_use_case = SettingsUserDataUseCase(
            redis_service=redis_service,
            users_service=users_service,
            notification_service=notification_service
        )
        self.menu_settings_use_case = MenuSettingsUseCase(
            users_service=users_service,
            translation_service=translation_service,
            canteens_service=canteens_service,
            telegram_interface=telegram_interface,
            settings_keyboards=settings_keyboards,
            update_user_data_use_case=self.settings_user_data_use_case,
        )

    async def menu_settings(self, callback, user_id: int, locale: str):
        await self.menu_settings_use_case.menu_settings(callback, user_id=user_id, locale=locale)

    async def change_locale(self, callback, user_id: int, new_locale: str):
        await self.menu_settings_use_case.change_locale(callback, user_id=user_id, new_locale=new_locale)

    async def menu_change_mailing_time(self, callback, locale: str):
        await self.menu_settings_use_case.menu_change_mailing_time(callback, locale=locale)

    async def change_mailing_time(self, callback, user_id: int, locale: str, new_mailing_time: str):
        await self.menu_settings_use_case.change_mailing_time(callback, user_id=user_id,
                                                              new_mailing_time=new_mailing_time, locale=locale)

    async def change_mailing_status(self, callback, user_id: int, locale: str):
        await self.menu_settings_use_case.change_mailing_status(callback, user_id=user_id, locale=locale)

    async def menu_change_canteen(self, callback, user_id: int, locale: str):
        await self.menu_settings_use_case.menu_change_canteen(callback, user_id=user_id, locale=locale)

    async def change_canteen(self, callback, user_id: int, locale: str, new_canteen_id: int):
        await self.menu_settings_use_case.change_canteen(callback, user_id=user_id,
                                                         locale=locale, new_canteen_id=new_canteen_id)

    async def set_new_locale(self, user_id: int, new_locale: str):
        await self.settings_user_data_use_case.update_locale(user_id=user_id, new_locale=new_locale)

    async def set_new_mailing_time(self, user_id: int, new_mailing_time: str):
        await self.settings_user_data_use_case.update_mailing_time(user_id=user_id, new_mailing_time=new_mailing_time)

    async def update_canteen_id(self, user_id: int, new_canteen_id: int):
        await self.settings_user_data_use_case.update_canteen_id(user_id=user_id, new_canteen_id=new_canteen_id)

    async def disable_mailing(self, user_id: int):
        await self.settings_user_data_use_case.disable_mailing(user_id=user_id)

    async def enable_mailing(self, user_id: int):
        await self.settings_user_data_use_case.enable_mailing(user_id=user_id)

    async def disable_user(self, user_id: int):
        await self.settings_user_data_use_case.disable_user(user_id=user_id)

    async def enable_user(self, user_id: int):
        await self.settings_user_data_use_case.enable_user(user_id=user_id)





