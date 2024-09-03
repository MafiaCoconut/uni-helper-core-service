from application.interfaces.telegram_interface import TelegramInterface
from application.services.canteens_service import CanteensService
from application.services.redis_service import RedisService
from application.services.settings_service import SettingsService
from application.services.translation_service import TranslationService
from application.services.users_service import UsersService
from application.use_cases.notification_send_canteens_menu_use_case import MailingSendCanteensMenuUseCase


class MailingService:
    def __init__(self,
                 redis_service: RedisService,
                 users_service: UsersService,
                 canteens_service: CanteensService,
                 settings_service: SettingsService,
                 telegram_interface: TelegramInterface,
                 translation_service: TranslationService,
                 ):
        self.notification_send_canteens_menu_use_case = MailingSendCanteensMenuUseCase(
            users_service=users_service,
            redis_service=redis_service,
            canteens_service=canteens_service,
            telegram_interface=telegram_interface,
            translation_service=translation_service,
            settings_service=settings_service
        )

    async def send_mailing_canteens_menu(self):
        await self.notification_send_canteens_menu_use_case.execute()