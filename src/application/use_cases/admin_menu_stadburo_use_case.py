from application.gateways.stadburo_gateway import StadburoGateway
from application.interfaces.telegram_interface import TelegramInterface
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder
from infrastructure.config.logs_config import log_decorator


class AdminMenuStadburoUseCase:
    def __init__(self,
                 stadburo_gateway: StadburoGateway,
                 telegram_interface: TelegramInterface,
                 admin_menu_keyboards: AdminMenuKeyboardsBuilder,
                 ):
        self.stadburo_gateway = stadburo_gateway
        self.telegram_interface = telegram_interface
        self.admin_menu_keyboards = admin_menu_keyboards

    @log_decorator(print_args=False, print_kwargs=False)
    async def menu(self, callback):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message="<b>Меню работы с stadburo</b>",
            keyboard=await self.admin_menu_keyboards.menu_stadburo(),
        )

    @log_decorator(print_args=False, print_kwargs=False)
    async def parse_all(self, callback):
        await self.stadburo_gateway.parse_stadburo_all()
        await callback.answer()
        try:
            await self.telegram_interface.edit_message_with_callback(
                callback=callback,
                message="<b>Меню работы с stadburo</b>\n\nПарсинг прошёл успешно",
                keyboard=await self.admin_menu_keyboards.menu_stadburo(),
            )
        except:
            pass
