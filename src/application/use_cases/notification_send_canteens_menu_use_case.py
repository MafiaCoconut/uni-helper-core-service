import logging
from datetime import datetime

from icecream import ic

from application.gateways.canteens_gateway import CanteensGateway
from application.gateways.users_gateway import UsersGateway
from application.interfaces.telegram_interface import TelegramInterface
from application.services.canteens_service import CanteensService
from application.services.notification_service import NotificationService
from application.services.redis_service import RedisService
from application.services.settings_service import SettingsService
from application.services.translation_service import TranslationService
from application.services.users_service import UsersService
from application.use_cases.generate_canteens_menu_use_case import GenerateCanteenMenuUseCase
from application.use_cases.send_canteens_menu_use_case import SendCanteensMenuUseCase
from application.use_cases.settings_user_data_use_case import SettingsUserDataUseCase
from domain.entities.user import User
from infrastructure.config.logs_config import log_decorator

error_logger = logging.getLogger("error_logger")
system_logger = logging.getLogger("system_logger")


class MailingSendCanteensMenuUseCase:
    def __init__(self,
                 users_service: UsersService,
                 redis_service: RedisService,
                 canteens_service: CanteensService,
                 telegram_interface: TelegramInterface,
                 translation_service: TranslationService,
                 settings_service: SettingsService,
                 ):
        self.users_service = users_service
        self.redis_service = redis_service
        self.canteens_service = canteens_service
        self.settings_service = settings_service
        self.generate_canteens_menu_use_case = GenerateCanteenMenuUseCase(
            canteens_gateway=canteens_service.canteens_gateway,
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
        system_logger.info(users)
        for user in users:

            if (
                    await self.check_status_user(user=user) and
                    await self.check_is_now_users_mailing_time(user=user) and
                    await self.check_status_canteen(canteen_id=user.canteen_id)
            ):
                try:
                    local_key = f"canteen_menu:{user.canteen_id}/{user.locale}"
                    if await self.redis_service.get(key=local_key):
                        system_logger.info(f'Canteen menu from Redis user{user.username}, canteen_id{user.canteen_id}, locale{user.locale}')
                        message = await self.redis_service.get(key=local_key)
                    else:
                        system_logger.info(f'Canteen menu from DB user{user.username}, canteen_id{user.canteen_id}, locale{user.locale}')
                        message = await self.generate_canteens_menu_use_case.execute(canteen_id=user.canteen_id, locale=user.locale)
                        await self.redis_service.setex(key=local_key, value=message, time=3600)

                    try:
                        await self.send_canteens_menu_use_case.execute(user_id=user.user_id, message=message, keyboard=None)
                    except Exception as e:
                        error_logger.error(f"The menu could not be sent to the user {user.user_id}. Error: {e}")
                        system_logger.error(f"The menu could not be sent to the user {user.user_id}. Error: {e}")
                        await self.settings_service.disable_user(user_id=user.user_id)
                except Exception as e:
                    system_logger.error(f"Случилась ошибка на пользователе: {user}")

    """
    TODO:
    1. Обращаемся к user api для получения объекта User + 
    2. Используя указанную для User столовую берём данные об этой столовой через api+ 
    3. Используя данные Canteen отдаём их классу рефактору данных в текст + 
    4. Полученный текст отдаём TelegramInterface для отправки конкретному User +
    """
    async def check_status_canteen(self, canteen_id: int):
        # system_logger.info(f'check_status_canteen: {canteen_id}')

        local_key = f'canteen_status:{canteen_id}'
        canteen_status = await self.redis_service.get(key=local_key)
        if canteen_status is not None:
            system_logger.info(f'From redis: {local_key}:{canteen_status}')
            if canteen_status == "active":
                return True
            else:
                return False
        else:
            canteen = await self.canteens_service.get_canteens_info(canteen_id=canteen_id)
            await self.redis_service.setex(key=local_key, value=canteen.status, time=3600)
            system_logger.info(f'From DB: {local_key}:{canteen_status}')
            if canteen.status == 'active':
                return True
            else:
                return False

    async def check_status_user(self, user: User):
        if user.status == "active" or user.mailing_time != '-':
            return True
        # system_logger.info(f'Ошибка отправки меню по причине статуса юзера: {user}')

        return False

    async def check_is_now_users_mailing_time(self, user: User):
        # system_logger.info(f'check_is_now_users_mailing_time: {user}')

        now = datetime.now()
        mailing_time_datetime_obj = datetime.strptime(user.mailing_time, "%H:%M")

        if (
                mailing_time_datetime_obj.hour == now.hour and
                now.minute <= mailing_time_datetime_obj.minute <= int(now.minute) + 2
        ):
            return True
        return False


