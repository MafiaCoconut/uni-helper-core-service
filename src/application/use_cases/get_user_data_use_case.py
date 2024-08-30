from application.gateways.users_gateway import UsersGateway
from infrastructure.config.logs_config import log_decorator


class GetUserDataUseCase:
    def __init__(self, users_gateway: UsersGateway):
        self.users_gateway = users_gateway

    @log_decorator(print_args=False, print_kwargs=False)
    async def get_users_locale(self, user_id: int):
        user = await self.users_gateway.get_user(user_id=user_id)
        return user.locale
