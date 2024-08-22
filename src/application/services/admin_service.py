from application.interfaces.telegram_interface import TelegramInterface
from application.providers.keyboards_provider import KeyboardsProvider
from application.telegram.keyboards.admin_keyboards import AdminKeyboardsBuilder
from application.use_cases.admin_menu_use_case import AdminMenuUseCase
from application.use_cases.send_message_to_admin_use_case import SendMessageToAdminUseCase
from domain.entities.user import User


class AdminsService:
    def __init__(self,
                 # keyboards_provider: KeyboardsProvider,
                 admin_keyboards: AdminKeyboardsBuilder,
                 telegram_interface: TelegramInterface,
                 ):
        # self.keyboards_provider = keyboards_provider

        self.send_message_to_admin_use_case = SendMessageToAdminUseCase(
            admin_keyboards=admin_keyboards,
            telegram_interface=telegram_interface,
        )
        self.admin_menu_use_case = AdminMenuUseCase()
        self.admin_menu_users_use_case = AdminMenuUsersUseCase()
        self.admin_menu_canteens_use_case = AdminMenuCanteensUseCase()
        self.admin_menu_stadburo_use_case = AdminMenuStadburoUseCase()
        self.admin_menu_logs_use_case = AdminMenuLogsUseCase()

    async def send_message_to_admin_about_new_user(self, user: User):
        await self.send_message_to_admin_use_case.new_users_info(user=user)

    async def send_menu_admin_main(self, user_id: int):

