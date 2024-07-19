from application.telegram.handlers.miss_message_handler import MissMessageHandler
from application.telegram.handlers.user_commands_handler import UserCommandsHandler
from application.telegram.handlers.menu_main_handlers import MenuMainHandler
from application.telegram.handlers.canteens_handlers import CanteensHandler
from application.telegram.handlers.donations_handlers import DonationsHandler

from infrastructure.config.keyboards_config import menu_main_keyboards, canteens_keyboards, navigator_keyboards

from infrastructure.config.services_config import translation_service


miss_message_handler = MissMessageHandler(translation_service=translation_service)
user_commands_handler = UserCommandsHandler(translation_service=translation_service)

menu_main_handler = MenuMainHandler(
    translation_service=translation_service,
    menu_main_keyboards=menu_main_keyboards,
)

canteens_handler = CanteensHandler(
    translation_service=translation_service,
    canteens_keyboards=canteens_keyboards,
)

donations_handler = DonationsHandler(
    translation_service=translation_service,
    navigator_keyboards=navigator_keyboards
)






