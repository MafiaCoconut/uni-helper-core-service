from application.gateways.stadburo_gateway import StadburoGateway
from application.interfaces.telegram_interface import TelegramInterface
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder


class AdminMenuStadburoUseCase:
    def __init__(self,
                 stadburo_gateway: StadburoGateway,
                 telegram_interface: TelegramInterface,
                 admin_menu_keyboards: AdminMenuKeyboardsBuilder,
                 ):
        self.stadburo_gateway = stadburo_gateway
        self.telegram_interface = telegram_interface
        self.admin_menu_keyboards = admin_menu_keyboards

    async def menu_main(self, user_id: int):
        await self.telegram_interface.send_message(
            user_id=user_id,
            message="<b>Меню работы с пользователями</b>",
            keyboard=await self.admin_menu_keyboards.menu_users(),
        )