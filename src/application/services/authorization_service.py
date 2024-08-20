from application.interfaces.telegram_interface import TelegramInterface
from application.services.admin_service import AdminsService
from application.services.canteens_service import CanteensService
from application.services.notification_service import NotificationService
from application.services.settings_service import SettingsService
from application.services.translation_service import TranslationService
from application.services.users_service import UsersService
from application.telegram.keyboards.authorization_keyboards import AuthorizationKeyboardsBuilder
from application.use_cases.authorization_use_case import AuthorizationUseCase
from domain.entities.user import User
from infrastructure.config.keyboards_config import menu_main_keyboards
from infrastructure.config.logs_config import log_decorator


class AuthorizationService:
    def __init__(self,
                 users_service: UsersService,
                 canteens_service: CanteensService,
                 telegram_interface: TelegramInterface,
                 admins_service: AdminsService,
                 settings_service: SettingsService,
                 notification_service: NotificationService,
                 authorization_keyboards: AuthorizationKeyboardsBuilder,
                 translation_service: TranslationService,
                 ):
        self.users_service = users_service
        self.canteens_service = canteens_service
        self.settings_service = settings_service
        self.authorization_use_case = AuthorizationUseCase(
            telegram_interface=telegram_interface,
            users_service=users_service,
            canteens_service=canteens_service,
            admins_service=admins_service,
            notification_service=notification_service,
            translation_service=translation_service,
            authorization_keyboards=authorization_keyboards,
            menu_main_keyboards=menu_main_keyboards,
        )

    @log_decorator
    async def start_authorization(self, user_id: int, name: str = "5",
                                  username: str = "-", locale: str = "en"
                                  ) -> int:
        message_id = await self.authorization_use_case.start_authorization(
            user_id=user_id,
            name=name,
            username=username,
            locale=locale,
        )
        return message_id

    @log_decorator
    async def refresh_menu_authorization(self, callback, user: User):
        await self.authorization_use_case.refresh_menu_authorization(callback=callback, user=user)

    @log_decorator
    async def user_already_exist(self, user: User) -> int:
        """
        Функция отправляет сообщение зарегистрированному пользователю о том что он уже зарегистрирован
        :param user: User(user_id, locale)
        :return: Message ID отправленного сообщения
        """
        message_id = await self.authorization_use_case.user_already_exist(user=user)
        return message_id

    @log_decorator
    async def start_canteen_config(self, user: User, menu_authorization_message_id: int) -> int:
        message_id = await self.authorization_use_case.start_canteen_config(
            menu_authorization_message_id=menu_authorization_message_id, user=user
        )
        return message_id

    @log_decorator
    async def set_new_locale(self, user_id: int, new_locale: str):
        await self.settings_service.set_new_locale(user_id=user_id, new_locale=new_locale)

    @log_decorator
    async def check_canteen(self, callback, user: User, canteen_id: int):
        await self.authorization_use_case.check_canteen(callback=callback, user=user, canteen_id=canteen_id)

    @log_decorator
    async def set_canteen(self, user: User, canteen_id: int, canteens_config_message_id: int) -> int:
        message_id = await self.authorization_use_case.set_canteen(
            user=user, canteen_id=canteen_id, canteens_config_message_id=canteens_config_message_id,
        )
        return message_id
