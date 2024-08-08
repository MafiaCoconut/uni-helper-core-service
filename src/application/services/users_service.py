from application.gateways.users_gateway import UsersGateway
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
