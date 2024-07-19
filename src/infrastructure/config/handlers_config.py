from application.telegram.handlers.logs_handler import LogsHandler
from application.telegram.handlers.miss_message_handler import MissMessageHandler
from application.telegram.handlers.user_commands_handler import UserCommandsHandler
from application.telegram.handlers.menu_main_handler import MenuMainHandler
from application.telegram.handlers.canteens_handler import CanteensHandler
from application.telegram.handlers.donations_handler import DonationsHandler

from infrastructure.config.keyboards_config import menu_main_keyboards, canteens_keyboards, navigator_keyboards

from infrastructure.config.services_config import translation_service, canteens_service

miss_message_handler = MissMessageHandler(translation_service=translation_service)

user_commands_handler = UserCommandsHandler(
    translation_service=translation_service,
    menu_main_keyboards=menu_main_keyboards
)

menu_main_handler = MenuMainHandler(
    translation_service=translation_service,
    menu_main_keyboards=menu_main_keyboards,
)

canteens_handler = CanteensHandler(
    translation_service=translation_service,
    canteens_keyboards=canteens_keyboards,
    canteens_service=canteens_service
)

donations_handler = DonationsHandler(
    translation_service=translation_service,
    navigator_keyboards=navigator_keyboards
)

logs_handler = LogsHandler()




