from application.interfaces.web_interface import WebInterface
from application.use_cases.get_user_data_use_case import GetUserDataUseCase


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
