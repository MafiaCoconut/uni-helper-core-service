from application.gateways.canteens_gateway import CanteensGateway
from application.gateways.stadburo_gateway import StadburoGateway
from application.gateways.users_gateway import UsersGateway
from application.interfaces.excel_interface import ExcelInterface
from application.interfaces.telegram_interface import TelegramInterface
from application.providers.keyboards_provider import KeyboardsProvider
from application.services.canteens_service import CanteensService
from application.services.settings_service import SettingsService
from application.services.stadburo_service import StadburoService
from application.services.users_service import UsersService
from application.telegram.keyboards.admin_keyboards import AdminKeyboardsBuilder
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder
from application.use_cases.admin_menu_canteens_use_case import AdminMenuCanteensUseCase
from application.use_cases.admin_menu_logs_use_case import AdminMenuLogsUseCase
from application.use_cases.admin_menu_mailing_use_case import AdminMenuMailingUseCase
from application.use_cases.admin_menu_stadburo_use_case import AdminMenuStadburoUseCase
from application.use_cases.admin_menu_use_case import AdminMenuUseCase
from application.use_cases.admin_menu_users_use_case import AdminMenuUsersUseCase
from application.use_cases.refactor_canteens_menu_to_text_use_case import RefactorCanteensMenuToTextUseCase
from application.use_cases.send_admins_mailing_text_use_case import SendAdminsMailingTextUseCase
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
                 users_service: UsersService,
                 canteens_service: CanteensService,
                 stadburo_service: StadburoService,
                 settings_service: SettingsService,
                 ):
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
            users_service=users_service,
            telegram_interface=telegram_interface,
            excel_interface=excel_interface,
            admin_keyboards=admin_keyboards,
            admin_menu_keyboards=admin_menu_keyboards,
        )
        self.admin_menu_canteens_use_case = AdminMenuCanteensUseCase(
            canteens_service=canteens_service,
            settings_service=settings_service,
            telegram_interface=telegram_interface,
            translation_service=translation_service,
            users_service=users_service,
            admin_menu_keyboards=admin_menu_keyboards,
            refactor_canteen_to_text=self.refactor_canteen_to_text,
        )

        self.admin_menu_stadburo_use_case = AdminMenuStadburoUseCase(
            stadburo_service=stadburo_service,
            telegram_interface=telegram_interface,
            admin_menu_keyboards=admin_menu_keyboards,
        )
        self.admin_menu_logs_use_case = AdminMenuLogsUseCase(
            telegram_interface=telegram_interface,
            admin_menu_keyboards=admin_menu_keyboards,
        )
        self.send_admins_mailing_text_use_case = SendAdminsMailingTextUseCase(
            users_service=users_service,
            telegram_interface=telegram_interface,
            settings_service=settings_service,
        )
        self.admin_menu_mailing_use_case = AdminMenuMailingUseCase(
            telegram_interface=telegram_interface,
            admin_menu_keyboards=admin_menu_keyboards,
            send_admins_mailing_text_use_case=self.send_admins_mailing_text_use_case
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

    async def change_canteen_status(self, callback, canteen_id: int):
        await self.admin_menu_canteens_use_case.change_canteen_status(callback=callback, canteen_id=canteen_id)

    async def menu_stadburo(self, callback):
        await self.admin_menu_stadburo_use_case.menu(callback=callback)

    async def parse_stadburo_all(self, callback):
        await self.admin_menu_stadburo_use_case.parse_all(callback=callback)

    async def menu_logs(self, callback):
        await self.admin_menu_logs_use_case.menu(callback=callback)

    async def send_logs(self, callback):
        await self.admin_menu_logs_use_case.send_logs(callback=callback)

    async def clear_logs(self, callback):
        await self.admin_menu_logs_use_case.clear_logs(callback=callback)

    async def menu_mailing(self, callback):
        await self.admin_menu_mailing_use_case.menu_mailing(callback)

    async def menu_get_mailing_text(self, callback, state):
        await self.admin_menu_mailing_use_case.menu_get_mailing_text(callback, state)

    async def menu_refactor_mailing_text_after_message(self, message, state, mailing_text: str):
        await self.admin_menu_mailing_use_case.menu_refactor_mailing_text_after_message(message, state, mailing_text)

    async def menu_refactor_mailing_text_after_callback(self, callback, state):
        await self.admin_menu_mailing_use_case.menu_refactor_mailing_text_after_callback(callback, state)


    async def menu_check_send_mailing_text(self, callback, state):
        await self.admin_menu_mailing_use_case.menu_check_send_mailing_text(callback, state)

    async def send_admin_mailing_text(self, callback, state):
        await self.admin_menu_mailing_use_case.send_admin_mailing_text(callback, state)







