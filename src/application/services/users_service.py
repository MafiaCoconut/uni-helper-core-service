from application.interfaces.web_interface import WebInterface
from application.use_cases.get_user_data_use_case import GetUserDataUseCase
from domain.entities.user import User


class UsersService:
    def __init__(self,
                 web_interface: WebInterface,
                 ):
        self.web_interface = web_interface
        self.get_user_data_use_case = GetUserDataUseCase(web_interface=web_interface)

    async def get_users_locale(self, user_id: int):
        return await self.get_user_data_use_case.get_users_locale(user_id=user_id)

    async def check_existence(self, user_id: int):
        return await self.web_interface.user_check_existence(user_id=user_id)

    async def save_user(self, user: User):
        await self.web_interface.create_user(user=user)

    async def update_user(self,
                          user_id: int,
                          new_status: str = None,
                          new_locale: str = None,
                          new_mailing_time: str = None,
                          new_canteen_id: int = None
                          ):
        await self.web_interface.update_user_data(
            user_id=user_id,
            new_status=new_status,
            new_mailing_time=new_mailing_time,
            new_locale=new_locale,
            new_canteen_id=new_canteen_id
        )

    async def get_user(self, user_id: int):
        return await self.web_interface.get_user(user_id=user_id)




