from datetime import datetime
import logging
from icecream import ic

from application.interfaces.telegram_interface import TelegramInterface
from application.services.canteens_service import CanteensService
from application.services.settings_service import SettingsService
from application.services.translation_service import TranslationService
from application.services.users_service import UsersService
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder
from application.use_cases.refactor_canteens_menu_to_text_use_case import RefactorCanteensMenuToTextUseCase
from infrastructure.config.logs_config import log_decorator

error_logger = logging.getLogger('error_logger')
system_logger = logging.getLogger('system_logger')


class AdminMenuCanteensUseCase:
    def __init__(self,
                 canteens_service: CanteensService,
                 users_service: UsersService,
                 settings_service: SettingsService,
                 telegram_interface: TelegramInterface,
                 translation_service: TranslationService,
                 admin_menu_keyboards: AdminMenuKeyboardsBuilder,
                 refactor_canteen_to_text: RefactorCanteensMenuToTextUseCase,
                 ):
        self.canteens_service = canteens_service
        self.users_service = users_service
        self.settings_service = settings_service
        self.translation_service = translation_service
        self.telegram_interface = telegram_interface
        self.admin_menu_keyboards = admin_menu_keyboards
        self.refactor_canteen_to_text = refactor_canteen_to_text

    async def menu(self, callback):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message="<b>Меню работы со столовыми</b>",
            keyboard=await self.admin_menu_keyboards.menu_canteens(),
        )

    @log_decorator(print_args=False, print_kwargs=False)
    async def parse(self, callback, canteen_id: int):
        await self.canteens_service.parse_canteen(canteen_id=canteen_id)
        try:
            await self.telegram_interface.edit_message_with_callback(
                callback=callback,
                message=f"<b>Меню работы со столовыми</b>\n\n"
                        f"Успешно прошёл парсинг\n\n"
                        f"Время парсинга: {datetime.now()}",
                keyboard=await self.admin_menu_keyboards.menu_canteens(),
            )
        except:
            pass
        await callback.answer()

    @log_decorator(print_args=False, print_kwargs=False)
    async def parse_all(self, callback):
        await self.canteens_service.parse_canteen_all()
        try:
            await self.telegram_interface.edit_message_with_callback(
                callback=callback,
                message=f"<b>Меню работы со столовыми</b>\n\n"
                        f"Парсинг запущен в автономном режиме\n\n"
                        f"Время начала парсинга: {datetime.now()}",
                keyboard=await self.admin_menu_keyboards.menu_canteens(),
            )
        except:
            pass
        # await callback.answer()

    @log_decorator(print_args=False, print_kwargs=False)
    async def get_menu(self, callback, canteen_id: int):
        data = await self.canteens_service.get_canteens_data(canteen_id=canteen_id)
        canteen = data.get("canteen")
        text = ""
        text += (f"Столовая: {canteen.name}\n"
                 f"Описание: {canteen.description}\n"
                 f"Статус: {canteen.status}\n"
                 f"Времена парсинга:\n"
                 f"     {canteen.times.get('v1').get('hour')}:{canteen.times.get('v1').get('minute')}\n"
                 f"     {canteen.times.get('v2').get('hour')}:{canteen.times.get('v2').get('minute')}\n"
                 f"     {canteen.times.get('v3').get('hour')}:{canteen.times.get('v3').get('minute')}\n"
                 f"Время открытия: {canteen.opened_time}\n"
                 f"Время закрытия: {canteen.closed_time}\n\n")

        data = await self.refactor_canteen_to_text.execute(
            canteen=data.get("canteen"),
            main_dishes=data.get("main_dishes"),
            side_dishes=data.get("side_dishes"),
            locale="ru",
            test_day=3,
            test_time=720,
        )
        text += data.get("text")

        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message=text,
            keyboard=await self.admin_menu_keyboards.menu_canteens(),
        )

    @log_decorator(print_args=False, print_kwargs=False)
    async def change_canteen_status(self, callback, canteen_id: int):
        canteen = await self.canteens_service.get_canteens_info(canteen_id=canteen_id)
        kwargs = {}
        if canteen.status == "active":
            await self.canteens_service.deactivate(canteen_id=canteen_id)
            message_id = "canteen-deactivated"
        else:
            await self.canteens_service.reactivate(canteen_id=canteen_id)
            message_id = "canteen-reactivated"
            kwargs["canteen_name"] = canteen.name

        updated_canteen = await self.canteens_service.get_canteens_info(canteen_id=canteen_id)

        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message=f"<b>Меню работы со столовыми</b>\n\n"
                    f"Столовая: {updated_canteen.name}\n"
                    f"Описание: {updated_canteen.description}\n"
                    f"Статус: {updated_canteen.status}\n"
                    f"Времена парсинга:\n"
                    f"     {updated_canteen.times.get('v1').get('hour')}:{updated_canteen.times.get('v1').get('minute')}\n"
                    f"     {updated_canteen.times.get('v2').get('hour')}:{updated_canteen.times.get('v2').get('minute')}\n"
                    f"     {updated_canteen.times.get('v3').get('hour')}:{updated_canteen.times.get('v3').get('minute')}\n"
                    f"Время открытия: {updated_canteen.opened_time}\n"
                    f"Время закрытия: {updated_canteen.closed_time}",
            keyboard=await self.admin_menu_keyboards.menu_canteens()
        )

        users = await self.users_service.get_users()
        for user in users:
            if user.canteen_id == canteen_id:
                try:
                    await self.telegram_interface.send_message(
                        user_id=user.user_id,
                        message=await self.translation_service.translate(message_id, user.locale, **kwargs)
                    )
                except Exception as e:
                    error_logger.error(f"The deactivate/reactivate canteen message could not be sent to the user {user.user_id}. Error: {e}")
                    system_logger.error(f"The deactivate/reactivate canteen message could not be sent to the user {user.user_id}. Error: {e}")
                    await self.settings_service.disable_user(user_id=user.user_id)



