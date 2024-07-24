from application.interfaces.telegram_interface import TelegramInterface
from application.interfaces.web_interface import WebInterface
from application.services.translation_service import TranslationService
from application.use_cases.refactor_canteens_menu_to_text_use_case import RefactorCanteensMenuToTextUseCase
from domain.entities.user import User


class GenerateAndSendCanteenMenu:
    def __init__(self,
                 web_interface: WebInterface,
                 telegram_interface: TelegramInterface,
                 translation_service: TranslationService
                 ):
        self.web_interface = web_interface
        self.telegram_interface = telegram_interface

        self.translation_service = translation_service
        self.refactor_canteens_menu_to_text_use_case = RefactorCanteensMenuToTextUseCase(
            translation_service=self.translation_service
        )

    async def execute(self, user_id: int):
        user = await self.web_interface.get_user(user_id=user_id)
        canteen_data = await self.web_interface.get_canteens_menu(canteen_id=user.canteen_id)
        await self.refactor_canteens_menu_to_text_use_case.execute(
            main_dishes=canteen_data.get('main_dishes'),
            side_dishes=canteen_data.get('side_dishes'),
            canteen=canteen_data.get('canteen'),
            locale=user.locale
        )






"""
Данные отправляются из Notification +
Core получает запрос с user_id +
Core берёт из USERS locale, canteen_id + 
CORE берёт из CANTEENS canteen_name, main_dishes, side_dishes +
CORE создаёт из данных CANTEENS текст
CORE отправляет пользователю созданный текст
"""
