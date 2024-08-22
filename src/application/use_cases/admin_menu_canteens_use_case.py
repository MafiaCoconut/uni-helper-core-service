from datetime import datetime

from application.gateways.canteens_gateway import CanteensGateway
from application.interfaces.telegram_interface import TelegramInterface
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder
from application.use_cases.refactor_canteens_menu_to_text_use_case import RefactorCanteensMenuToTextUseCase


class AdminMenuCanteensUseCase:
    def __init__(self,
                 canteens_gateway: CanteensGateway,
                 telegram_interface: TelegramInterface,
                 admin_menu_keyboards: AdminMenuKeyboardsBuilder,
                 refactor_canteen_to_text: RefactorCanteensMenuToTextUseCase,
                 ):
        self.canteens_gateway = canteens_gateway
        self.telegram_interface = telegram_interface
        self.admin_menu_keyboards = admin_menu_keyboards
        self.refactor_canteen_to_text = refactor_canteen_to_text

    async def menu(self, callback):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message="<b>Меню работы с пользователями</b>",
            keyboard=await self.admin_menu_keyboards.menu_canteens(),
        )

    async def parse(self, callback, canteen_id: int):
        await self.canteens_gateway.parse_canteen(canteen_id=canteen_id)
        try:
            await self.telegram_interface.edit_message_with_callback(
                callback=callback,
                message=f"<b>Меню работы с пользователями</b>\n\n"
                        f"Успешно прошёл парсинг\n\n"
                        f"Время парсинга: {datetime.now()}",
                keyboard=await self.admin_menu_keyboards.menu_canteens(),
            )
        except:
            pass
        await callback.answer()

    async def parse_all(self, callback):
        await self.canteens_gateway.parse_canteen_all()
        try:
            await self.telegram_interface.edit_message_with_callback(
                callback=callback,
                message=f"<b>Меню работы с пользователями</b>\n\n"
                        f"Успешно прошёл парсинг\n\n"
                        f"Время парсинга: {datetime.now()}",
                keyboard=await self.admin_menu_keyboards.menu_canteens(),
            )
        except:
            pass
        await callback.answer()

    async def get_menu(self, callback, canteen_id: int):
        data = await self.canteens_gateway.get_canteens_data(canteen_id=canteen_id)
        text = await self.refactor_canteen_to_text.execute(
            canteen=data.get("canteen"),
            main_dishes=data.get("main_dishes"),
            side_dishes=data.get("side_dishes"),
            locale="ru",
            test_day=3,
            test_time=720,
        )

        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message=text.get("text"),
            keyboard=await self.admin_menu_keyboards.menu_canteens(),
        )


