from icecream import ic

from application.interfaces.telegram_interface import TelegramInterface
from application.interfaces.web_interface import WebInterface
from application.services.translation_service import TranslationService
from application.use_cases.generate_canteens_menu_use_case import GenerateCanteenMenuUseCase
from application.use_cases.notification_send_canteens_menu_use_case import NotificationSendCanteensMenuUseCase
from application.use_cases.refactor_canteens_menu_to_text_use_case import RefactorCanteensMenuToTextUseCase
from domain.entities.canteen import Canteen


class CanteensService:
    def __init__(self,
                 web_interface: WebInterface,
                 telegram_interface: TelegramInterface,
                 translation_service: TranslationService,
                 ):
        self.web_interface = web_interface
        self.telegram_interface = telegram_interface
        self.translation_service = translation_service
        self.generate_canteens_menu = GenerateCanteenMenuUseCase(
            web_interface=self.web_interface,
            telegram_interface=self.telegram_interface,
            translation_service=self.translation_service,
        )
        self.notification_send_canteens_menu_use_case = NotificationSendCanteensMenuUseCase(
            web_interface=web_interface,
            telegram_interface=telegram_interface,
            translation_service=translation_service,
        )

    async def get_canteens_menu(self, canteen_id: int, locale: str) -> str:
        return await self.generate_canteens_menu.execute(canteen_id=canteen_id, locale=locale)

    async def get_canteens_info(self, canteen_id: int) -> Canteen:
        return await self.web_interface.get_canteens_info(canteen_id)

    async def parse_canteen(self, canteen_id: int) -> str:
        return await self.web_interface.parse_canteen(canteen_id)

    async def parse_canteen_all(self):
        await self.web_interface.parse_canteen_all()

    async def send_canteens_menu_to_user(self, user_id: int):
        await self.notification_send_canteens_menu_use_case.execute(user_id=user_id)


