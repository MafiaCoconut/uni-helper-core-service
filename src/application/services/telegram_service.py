from application.interfaces.telegram_interface import TelegramInterface
from application.interfaces.web_interface import WebInterface
from application.services.translation_service import TranslationService
from application.use_cases.generate_and_send_canteens_menu_use_case import GenerateAndSendCanteenMenu


class TelegramService:
    def __init__(self,
                 web_interface: WebInterface,
                 telegram_interface: TelegramInterface,
                 translation_service: TranslationService,

                 ):
        self.web_interface = web_interface
        self.telegram_interface = telegram_interface
        self.translation_service = translation_service
        self.generate_and_send_canteens_menu = GenerateAndSendCanteenMenu(
            web_interface=self.web_interface,
            telegram_interface=self.telegram_interface,
            translation_service=self.translation_service,
        )

    def send_canteens_menu(self, user_id: int):
        self.generate_and_send_canteens_menu.execute(user_id=user_id)
