# from application.interfaces.telegram_interface import TelegramInterface
# from application.interfaces.canteens_gateway import CanteesGateway
# from application.services.translation_service import TranslationService
# from application.use_cases.generate_canteens_menu_use_case import GenerateCanteenMenuUseCase
#
#
# class TelegramService:
#     def __init__(self,
#                  web_interface: CanteesGateway,
#                  telegram_interface: TelegramInterface,
#                  translation_service: TranslationService,
#
#                  ):
#         self.web_interface = web_interface
#         self.telegram_interface = telegram_interface
#         self.translation_service = translation_service
#         self.generate_and_send_canteens_menu = GenerateCanteenMenuUseCase(
#             web_interface=self.web_interface,
#             telegram_interface=self.telegram_interface,
#             translation_service=self.translation_service,
#         )
#
#     def send_canteens_menu(self, user_id: int):
#         self.generate_and_send_canteens_menu.execute(user_id=user_id)
