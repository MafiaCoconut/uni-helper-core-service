from application.interfaces.telegram_interface import TelegramInterface
from application.services.notification_service import NotificationService
from application.services.redis_service import RedisService
from application.services.users_service import UsersService
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from application.use_cases.settings_use_case import SettingsUseCase
from application.use_cases.update_user_data_use_case import SettingsUserDataUseCase
from domain.entities.user import User
from infrastructure.config.logs_config import log_decorator
from infrastructure.config.translation_config import translation_service


class SettingsService:
    def __init__(self,
                 users_service: UsersService,
                 redis_service: RedisService,
                 notification_service: NotificationService,
                 telegram_interface: TelegramInterface,
                 settings_keyboards: SettingsKeyboardsBuilder,
                 ):
        self.settings_keyboards = settings_keyboards
        self.telegram_interface = telegram_interface
        self.update_user_data_use_case = SettingsUserDataUseCase(
            redis_service=redis_service,
            users_service=users_service,
            notification_service=notification_service
        )
        self.settings_use_case = SettingsUseCase(
            users_service=users_service,
            translation_service=translation_service,
            telegram_interface=telegram_interface,
            settings_keyboards=settings_keyboards,
        )

    @log_decorator
    async def menu_settings(self, callback, user_id: int, locale: str):
        await self.settings_use_case.menu_settings(callback=callback, user_id=user_id, locale=locale)


    @log_decorator
    async def set_new_locale(self, user_id: int, new_locale: str):
        await self.update_user_data_use_case.update_locale(user_id=user_id, new_locale=new_locale)

    @log_decorator
    async def refresh_menu_settings(self, callback):
        pass


