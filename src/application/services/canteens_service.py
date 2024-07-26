from icecream import ic

from application.interfaces.telegram_interface import TelegramInterface
from application.interfaces.web_interface import WebInterface
from application.services.translation_service import TranslationService
from application.use_cases.generate_and_send_canteens_menu_use_case import GenerateAndSendCanteenMenu
from application.use_cases.refactor_canteens_menu_to_text_use_case import RefactorCanteensMenuToTextUseCase


class CanteensService:
    def __init__(self,
                 web_interface: WebInterface,
                 telegram_interface: TelegramInterface ,
                 translation_service: TranslationService,
                 ):
        self.web_interface = web_interface
        self.telegram_interface = telegram_interface
        self.translation_service = translation_service
        self.generate_and_send_canteen_menu = GenerateAndSendCanteenMenu(
            web_interface=self.web_interface,
            telegram_interface=self.telegram_interface,
            translation_service=self.translation_service,
        )

    async def get_canteens_menu(self, canteen_id: int) -> str:
        json_data = await self.web_interface.get_canteens_data(canteen_id)
        if json_data.get('error').get('type') == "Canteen is now closed":
            return json_data.get('error').get('text')
        else:
            return json_data.get('menu')

    async def get_canteens_info(self, canteen_id: int) -> str:
        return await self.web_interface.get_canteens_info(canteen_id)

    async def parse_canteen(self, canteen_id: int) -> str:
        return await self.web_interface.parse_canteen(canteen_id)

    async def parse_canteen_all(self):
        await self.web_interface.parse_canteen_all()

    async def send_canteen_info(self, user_id: int):
        await self.generate_and_send_canteen_menu.execute(user_id=user_id)


