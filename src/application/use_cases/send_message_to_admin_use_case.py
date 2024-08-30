from application.interfaces.telegram_interface import TelegramInterface
from application.telegram.keyboards.admin_keyboards import AdminKeyboardsBuilder
from domain.entities.user import User
from infrastructure.config.logs_config import log_decorator


class SendMessageToAdminUseCase:
    def __init__(self,
                 admin_keyboards: AdminKeyboardsBuilder,
                 telegram_interface: TelegramInterface,
                 ):
        self.admin_keyboards = admin_keyboards
        self.telegram_interface = telegram_interface

    @log_decorator(print_args=False, print_kwargs=False)
    async def new_users_info(self, user: User):
        await self.telegram_interface.send_message_to_admin(
            message=f"Добавлен пользователь:\n\n"
                    f"id: {user.user_id}\n"
                    f"username: @{user.username}\n"
                    f"name: {user.name}\n"
                    f"locale: {user.locale}",
            keyboard=await self.admin_keyboards.get_link_to_person(user_id=user.user_id)
        )


