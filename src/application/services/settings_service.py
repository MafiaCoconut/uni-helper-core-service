from application.services.redis_service import RedisService
from application.services.users_service import UsersService
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from application.use_cases.update_user_data_use_case import SettingsUserDataUseCase
from domain.entities.user import User
from infrastructure.config.logs_config import log_decorator


class SettingsService:
    def __init__(self,
                 users_service: UsersService,
                 redis_service: RedisService,
                 settings_keyboards: SettingsKeyboardsBuilder,
                 ):
        self.settings_keyboards = settings_keyboards
        self.update_user_data_use_case = SettingsUserDataUseCase(
            redis_service=redis_service,
            users_service=users_service,
        )

    @log_decorator
    async def set_new_locale(self, user_id: int, new_locale: str):
        await self.update_user_data_use_case.update_locale(user_id=user_id, new_locale=new_locale)

    @log_decorator
    async def refresh_menu_settings(self, callback):
        pass


