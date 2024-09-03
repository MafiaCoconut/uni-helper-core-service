from icecream import ic

from application.gateways.canteens_gateway import CanteensGateway
from application.gateways.users_gateway import UsersGateway
from application.interfaces.telegram_interface import TelegramInterface
from application.services.notification_service import NotificationService
from application.services.redis_service import RedisService
from application.services.translation_service import TranslationService
from application.services.users_service import UsersService
from application.use_cases.generate_canteens_menu_use_case import GenerateCanteenMenuUseCase
from application.use_cases.notification_send_canteens_menu_use_case import NotificationSendCanteensMenuUseCase
from application.use_cases.refactor_canteens_menu_to_text_use_case import RefactorCanteensMenuToTextUseCase
from application.use_cases.settings_user_data_use_case import SettingsUserDataUseCase
from domain.entities.canteen import Canteen


class CanteensService:
    def __init__(self,
                 users_service: UsersService,
                 notification_service: NotificationService,
                 canteens_gateway: CanteensGateway,
                 telegram_interface: TelegramInterface,
                 translation_service: TranslationService,
                 redis_service: RedisService,
                 ):
        self.canteens_gateway = canteens_gateway
        self.telegram_interface = telegram_interface
        self.translation_service = translation_service
        self.generate_canteens_menu = GenerateCanteenMenuUseCase(
            canteens_gateway=self.canteens_gateway,
            telegram_interface=self.telegram_interface,
            translation_service=self.translation_service,
        )
        self.settings_user_data_use_case = SettingsUserDataUseCase(
            redis_service=redis_service,
            users_service=users_service,
            notification_service=notification_service
        )
        self.notification_send_canteens_menu_use_case = NotificationSendCanteensMenuUseCase(
            users_service=users_service,
            redis_service=redis_service,
            canteens_gateway=canteens_gateway,
            telegram_interface=telegram_interface,
            translation_service=translation_service,
            settings_user_data_use_case=self.settings_user_data_use_case
        )

    async def get_canteens_menu(self, canteen_id: int, locale: str) -> str:
        return await self.generate_canteens_menu.execute(canteen_id=canteen_id, locale=locale)

    async def get_canteens_info(self, canteen_id: int) -> Canteen:
        return await self.canteens_gateway.get_canteens_info(canteen_id)

    async def parse_canteen(self, canteen_id: int) -> str:
        return await self.canteens_gateway.parse_canteen(canteen_id)

    async def parse_canteen_all(self):
        await self.canteens_gateway.parse_canteen_all()

    async def send_canteens_menu_to_user(self):
        await self.notification_send_canteens_menu_use_case.execute()


