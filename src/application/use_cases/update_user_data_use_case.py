from application.services.users_service import UsersService


class UpdateUserDataUseCase:
    def __init__(self,
                 users_service: UsersService,
                 redis_service: RedisService,
                 ):
        self.users_service = users_service
        self.redis_service = redis_service

    def update_locale(self, user_id: int, new_locale: str):
        """

        :param user_id:
        :param new_locale:
        :return:
        """

        """
        1. Отправить в User Service новые данные
        2. Обновить locale в redis
        """
