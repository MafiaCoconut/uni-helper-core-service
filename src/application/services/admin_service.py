from application.interfaces.telegram_interface import TelegramInterface
from application.providers.keyboards_provider import KeyboardsProvider
from application.telegram.keyboards.admin_keyboards import AdminKeyboardsBuilder
from application.use_cases.send_message_to_admin_use_case import SendMessageToAdminUseCase
from domain.entities.user import User


class AdminsService:
    def __init__(self,
                 keyboards_provider: KeyboardsProvider,
                 telegram_interface: TelegramInterface,
                 ):
        self.keyboards_provider = keyboards_provider

        self.send_message_to_admin_use_case = SendMessageToAdminUseCase(
            admin_keyboards=self.admin_keyboards,
            telegram_interface=telegram_interface,
        )

    @property
    def admin_keyboards(self):
        return self.keyboards_provider.get_admin_keyboards()

    async def send_message_to_admin_about_new_user(self, user: User):
        await self.send_message_to_admin_use_case.new_users_info(user=user)


