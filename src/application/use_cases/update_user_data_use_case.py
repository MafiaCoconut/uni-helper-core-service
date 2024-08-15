from application.services.notification_service import NotificationService
from application.services.redis_service import RedisService
from application.services.users_service import UsersService


class SettingsUserDataUseCase:
    def __init__(self,
                 users_service: UsersService,
                 redis_service: RedisService,
                 notification_service: NotificationService
                 ):
        self.users_service = users_service
        self.redis_service = redis_service
        self.notification_service = notification_service

    async def update_locale(self, user_id: int, new_locale: str):
        """
        Функция обновляет локаль пользователя в базе данных и Redis
        :param user_id: ID юзера в телеграм
        :param new_locale: Языковая локаль
        :return: None
        """
        await self.users_service.update_user(user_id=user_id, new_locale=new_locale)
        await self.redis_service.setex(key=f"{user_id}:locale", value=new_locale, time=3600)

    async def update_mailing_time(self, user_id: int, new_mailing_time: str):
        await self.users_service.update_user(user_id=user_id, new_mailing_time=new_mailing_time)

    async def update_canteen_id(self, user_id: int, new_canteen_id: int):
        await self.users_service.update_user(user_id=user_id, new_canteen_id=new_canteen_id)

    async def disable_mailing(self, user_id: int):
        await self.users_service.update_user(user_id=user_id, new_mailing_time='-')
        await self.notification_service.delete_job(user_id=user_id)



