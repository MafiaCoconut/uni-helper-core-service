from application.interfaces.telegram_interface import TelegramInterface
from application.interfaces.web_interface import WebInterface
from application.services.translation_service import TranslationService
from application.use_cases.generate_canteens_menu_use_case import GenerateCanteenMenuUseCase
from application.use_cases.send_canteens_menu_use_case import SendCanteensMenuUseCase


class NotificationSendCanteensMenuUseCase:
    def __init__(self,
                 web_interface: WebInterface,
                 telegram_interface: TelegramInterface,
                 translation_service: TranslationService,
                 ):
        self.web_interface = web_interface
        self.generate_canteens_menu_use_case = GenerateCanteenMenuUseCase(
            web_interface=web_interface,
            telegram_interface=telegram_interface,
            translation_service=translation_service
        )
        self.send_canteens_menu_use_case = SendCanteensMenuUseCase(
            telegram_interface=telegram_interface
        )

    async def execute(self, user_id: int):
        """
        Функция получает данные о выбранной User столовой и локали,
        преобразует текущие данные столовой в текст и возвращает их в виде текста
        :param user_id: ID юзера в базе данных
        """
        user = await self.web_interface.get_user(user_id=user_id)
        message = await self.generate_canteens_menu_use_case.execute(canteen_id=user.canteen_id, locale=user.locale)
        await self.send_canteens_menu_use_case.execute(user_id=user_id, message=message, keyboard=None)


    """
    TODO:
    1. Обращаемся к user api для получения объекта User + 
    2. Используя указанную для User столовую берём данные об этой столовой через api+ 
    3. Используя данные Canteen отдаём их классу рефактору данных в текст + 
    4. Полученный текст отдаём TelegramInterface для отправки конкретному User +
    """