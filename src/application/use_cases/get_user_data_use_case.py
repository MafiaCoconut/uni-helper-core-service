from application.interfaces.web_interface import WebInterface


class GetUserDataUseCase:
    def __init__(self, web_interface: WebInterface):
        self.web_interface = web_interface

    async def get_users_locale(self, user_id: int):
        user = await self.web_interface.get_user(user_id=user_id)
        return user.locale
