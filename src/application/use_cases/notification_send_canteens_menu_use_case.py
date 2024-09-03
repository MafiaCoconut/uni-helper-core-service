import logging
from datetime import datetime

from application.gateways.canteens_gateway import CanteensGateway
from application.gateways.users_gateway import UsersGateway
from application.interfaces.telegram_interface import TelegramInterface
from application.services.notification_service import NotificationService
from application.services.redis_service import RedisService
from application.services.translation_service import TranslationService
from application.services.users_service import UsersService
from application.use_cases.generate_canteens_menu_use_case import GenerateCanteenMenuUseCase
from application.use_cases.send_canteens_menu_use_case import SendCanteensMenuUseCase
from application.use_cases.settings_user_data_use_case import SettingsUserDataUseCase
from infrastructure.config.logs_config import log_decorator

error_logger = logging.getLogger("error_logger")
system_logger = logging.getLogger("system_logger")


class NotificationSendCanteensMenuUseCase:
    def __init__(self,
                 users_service: UsersService,
                 redis_service: RedisService,
                 canteens_gateway: CanteensGateway,
                 telegram_interface: TelegramInterface,
                 translation_service: TranslationService,
                 settings_user_data_use_case: SettingsUserDataUseCase,
                 ):
        self.users_service = users_service
        self.redis_service = redis_service
        self.settings_user_data_use_case = settings_user_data_use_case
        self.generate_canteens_menu_use_case = GenerateCanteenMenuUseCase(
            canteens_gateway=canteens_gateway,
            telegram_interface=telegram_interface,
            translation_service=translation_service
        )
        self.send_canteens_menu_use_case = SendCanteensMenuUseCase(
            telegram_interface=telegram_interface
        )

    @log_decorator(print_args=False)
    async def execute(self):
        """
        Функция получает данные о выбранной User столовой и локали,
        преобразует текущие данные столовой в текст и возвращает их в виде текста
        :param user_id: ID юзера в базе данных
        """
        users = await self.users_service.get_users()
        for user in users:
            now = datetime.now()
            if user.status == "active" or user.mailing_time != '-':
                user_mailing_time_datetime_obj = datetime.strptime(user.mailing_time, "%H:%M")

                if (user_mailing_time_datetime_obj.hour == now.hour and
                        now.minute <= user_mailing_time_datetime_obj.minute <= int(now.minute) + 2):
                    local_key = f"canteen_menu:{user.canteen_id}/{user.locale}"
                    if await self.redis_service.get(key=local_key):
                        message = await self.redis_service.get(key=local_key)
                    else:
                        message = await self.generate_canteens_menu_use_case.execute(canteen_id=user.canteen_id, locale=user.locale)
                        await self.redis_service.setex(key=local_key, value=message, time=3600)

                    try:
                        await self.send_canteens_menu_use_case.execute(user_id=user.user_id, message=message, keyboard=None)
                    except Exception as e:
                        error_logger.error(f"The menu could not be sent to the user. Error: {e}")
                        system_logger.error(f"The menu could not be sent to the user. Error: {e}")
                        await self.settings_user_data_use_case.disable_user(user_id=user.user_id)

    """
    TODO:
    1. Обращаемся к user api для получения объекта User + 
    2. Используя указанную для User столовую берём данные об этой столовой через api+ 
    3. Используя данные Canteen отдаём их классу рефактору данных в текст + 
    4. Полученный текст отдаём TelegramInterface для отправки конкретному User +
    """