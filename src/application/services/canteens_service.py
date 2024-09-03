from application.gateways.canteens_gateway import CanteensGateway
from application.interfaces.telegram_interface import TelegramInterface
from application.services.translation_service import TranslationService
from application.use_cases.generate_canteens_menu_use_case import GenerateCanteenMenuUseCase
from domain.entities.canteen import Canteen


class CanteensService:
    def __init__(self,
                 translation_service: TranslationService,
                 canteens_gateway: CanteensGateway,
                 telegram_interface: TelegramInterface,
                 ):
        self.canteens_gateway = canteens_gateway
        self.telegram_interface = telegram_interface
        self.translation_service = translation_service
        self.generate_canteens_menu = GenerateCanteenMenuUseCase(
            canteens_gateway=self.canteens_gateway,
            telegram_interface=self.telegram_interface,
            translation_service=self.translation_service,
        )

    async def get_canteens_menu(self, canteen_id: int, locale: str) -> str:
        return await self.generate_canteens_menu.execute(canteen_id=canteen_id, locale=locale)

    async def get_canteens_info(self, canteen_id: int) -> Canteen:
        return await self.canteens_gateway.get_canteens_info(canteen_id)

    async def parse_canteen(self, canteen_id: int) -> str:
        return await self.canteens_gateway.parse_canteen(canteen_id)

    async def parse_canteen_all(self):
        await self.canteens_gateway.parse_canteen_all()



