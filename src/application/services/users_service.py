from application.gateways.users_gateway import UsersGateway
from application.services.redis_service import RedisService
from application.use_cases.get_user_data_use_case import GetUserDataUseCase
from domain.entities.user import User


class UsersService:
    def __init__(self,
                 users_gateway: UsersGateway,
                 ):
        self.users_gateway = users_gateway
        self.get_user_data_use_case = GetUserDataUseCase(users_gateway=users_gateway)

    async def get_users_locale(self, user_id: int):
        return await self.get_user_data_use_case.get_users_locale(user_id=user_id)

    async def check_existence(self, user_id: int):
        return await self.users_gateway.user_check_existence(user_id=user_id)

    async def check_status(self, user_id: int):
        user = await self.users_gateway.get_user(user_id=user_id)
        return user.status

    async def create_user(self, user: User):
        await self.users_gateway.create_user(user=user)

    async def update_user(
            self, user_id: int,
            new_status: str = None, new_locale: str = None, new_mailing_time: str = None, new_canteen_id: int = None
    ):
        await self.users_gateway.update_user_data(
            user_id=user_id,
            new_status=new_status,
            new_mailing_time=new_mailing_time,
            new_locale=new_locale,
            new_canteen_id=new_canteen_id
        )

    async def get_user(self, user_id: int):
        return await self.users_gateway.get_user(user_id=user_id)

    async def reactivate_user(self, user_id: int):
        await self.users_gateway.reactivate_user(user_id=user_id)

    async def deactivate_user(self, user_id: int):
        await self.users_gateway.deactivate_user(user_id=user_id)

