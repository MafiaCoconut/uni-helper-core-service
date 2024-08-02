from application.services.authorization_service import AuthorizationService
from application.services.redis_service import RedisService
from application.services.users_service import UsersService
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from application.use_cases.update_user_data_use_case import UpdateUserDataUseCase
from domain.entities.user import User
from infrastructure.config.logs_config import log_decorator


class SettingsService:
    def __init__(self,
                 users_service: UsersService,
                 redis_service: RedisService,
                 authorization_service: AuthorizationService,
                 settings_keyboards: SettingsKeyboardsBuilder,
                 ):
        self.authorization_service = authorization_service
        self.settings_keyboards = settings_keyboards
        self.update_user_data_use_case = UpdateUserDataUseCase(
            redis_service=redis_service,
            users_service=users_service,
        )

    @log_decorator
    async def set_new_locale(self, user_id: int, new_locale: str):
        await self.update_user_data_use_case.update_locale(user_id=user_id, new_locale=new_locale)

    @log_decorator
    async def send_menu_where_was_called(self, callback, where_was_called: str, user: User):
        match where_was_called:
            case "menu_authorization":
                await self.authorization_service.refresh_menu_authorization(callback=callback, user=user)
            case "menu_settings":
                pass

    @log_decorator
    async def refresh_menu_settings(self, callback):
        pass


