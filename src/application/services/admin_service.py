from application.gateways.canteens_gateway import CanteensGateway
from application.gateways.stadburo_gateway import StadburoGateway
from application.gateways.users_gateway import UsersGateway
from application.interfaces.excel_interface import ExcelInterface
from application.interfaces.telegram_interface import TelegramInterface
from application.providers.keyboards_provider import KeyboardsProvider
from application.telegram.keyboards.admin_keyboards import AdminKeyboardsBuilder
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder
from application.use_cases.admin_menu_canteens_use_case import AdminMenuCanteensUseCase
from application.use_cases.admin_menu_logs_use_case import AdminMenuLogsUseCase
from application.use_cases.admin_menu_stadburo_use_case import AdminMenuStadburoUseCase
from application.use_cases.admin_menu_use_case import AdminMenuUseCase
from application.use_cases.admin_menu_users_use_case import AdminMenuUsersUseCase
from application.use_cases.refactor_canteens_menu_to_text_use_case import RefactorCanteensMenuToTextUseCase
from application.use_cases.send_message_to_admin_use_case import SendMessageToAdminUseCase
from domain.entities.user import User
from infrastructure.config.translation_config import translation_service


class AdminsService:
    def __init__(self,
                 # keyboards_provider: KeyboardsProvider,
                 admin_keyboards: AdminKeyboardsBuilder,
                 admin_menu_keyboards: AdminMenuKeyboardsBuilder,
                 telegram_interface: TelegramInterface,
                 excel_interface: ExcelInterface,
                 users_gateway: UsersGateway,
                 canteens_gateway: CanteensGateway,
                 stadburo_gateway: StadburoGateway,

                 ):
        # self.keyboards_provider = keyboards_provider
        self.refactor_canteen_to_text = RefactorCanteensMenuToTextUseCase(
            translation_service=translation_service
        )
        self.send_message_to_admin_use_case = SendMessageToAdminUseCase(
            admin_keyboards=admin_keyboards,
            telegram_interface=telegram_interface,
        )
        self.admin_menu_use_case = AdminMenuUseCase(
            telegram_interface=telegram_interface,
            admin_menu_keyboards=admin_menu_keyboards,
        )
        self.admin_menu_users_use_case = AdminMenuUsersUseCase(
            users_gateway=users_gateway,
            telegram_interface=telegram_interface,
            excel_interface=excel_interface,
            admin_keyboards=admin_keyboards,
            admin_menu_keyboards=admin_menu_keyboards,
        )
        self.admin_menu_canteens_use_case = AdminMenuCanteensUseCase(
            canteens_gateway=canteens_gateway,
            telegram_interface=telegram_interface,
            admin_menu_keyboards=admin_menu_keyboards,
            refactor_canteen_to_text=self.refactor_canteen_to_text
        )

        self.admin_menu_stadburo_use_case = AdminMenuStadburoUseCase(
            stadburo_gateway=stadburo_gateway,
            telegram_interface=telegram_interface,
            admin_menu_keyboards=admin_menu_keyboards,
        )
        self.admin_menu_logs_use_case = AdminMenuLogsUseCase(
            telegram_interface=telegram_interface,
            admin_menu_keyboards=admin_menu_keyboards,
        )

    async def send_message_to_admin_about_new_user(self, user: User):
        await self.send_message_to_admin_use_case.new_users_info(user=user)

    async def send_menu_main(self, user_id: int):
        await self.admin_menu_use_case.send_menu_main(user_id=user_id)

    async def menu_main(self, callback):
        await self.admin_menu_use_case.menu_main(callback=callback)

    async def menu_users(self, callback):
        await self.admin_menu_users_use_case.menu(callback=callback)

    async def get_all_users_data(self, callback):
        await self.admin_menu_users_use_case.get_all_users_data_in_xslx(callback=callback)

    async def get_count_users(self, callback):
        await self.admin_menu_users_use_case.get_count_users(callback=callback)

    async def request_to_user_data(self, callback, state):
        await self.admin_menu_users_use_case.request_to_user_data(callback=callback, state=state)

    async def get_user_data(self, message, state, user_id: int):
        await self.admin_menu_users_use_case.get_user_data(message=message, state=state, user_id=user_id)

    async def menu_canteens(self, callback):
        await self.admin_menu_canteens_use_case.menu(callback=callback)

    async def parse_canteen(self, callback, canteen_id: int):
        await self.admin_menu_canteens_use_case.parse(callback=callback, canteen_id=canteen_id)

    async def parse_canteen_all(self, callback):
        await self.admin_menu_canteens_use_case.parse_all(callback=callback)

    async def get_canteen(self, callback, canteen_id: int):
        await self.admin_menu_canteens_use_case.get_menu(callback=callback, canteen_id=canteen_id)



    async def menu_stadburo(self, callback):
        await self.admin_menu_stadburo_use_case.menu(callback=callback)

    async def menu_logs(self, callback):
        await self.admin_menu_logs_use_case.menu(callback=callback)




