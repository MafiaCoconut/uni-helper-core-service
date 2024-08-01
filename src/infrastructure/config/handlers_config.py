from application.telegram.handlers.authorization_handler import AuthorizationHandler
from application.telegram.handlers.links_handler import LinksHandler
from application.telegram.handlers.logs_handler import LogsHandler
from application.telegram.handlers.miss_message_handler import MissMessageHandler
from application.telegram.handlers.user_commands_handler import UserCommandsHandler
from application.telegram.handlers.menu_main_handler import MenuMainHandler
from application.telegram.handlers.canteens_handler import CanteensHandler
from application.telegram.handlers.donations_handler import DonationsHandler
from application.telegram.handlers.stadburo_handler import StadburoHandler

from infrastructure.config.keyboards_config import menu_main_keyboards, canteens_keyboards, navigator_keyboards, \
    stadburo_keyboards, links_keyboards

from infrastructure.config.services_config import translation_service, canteens_service, stadburo_service, users_service

miss_message_handler = MissMessageHandler(translation_service=translation_service)

authorization_handler = AuthorizationHandler(
    users_service=users_service
)

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

stadburo_handler = StadburoHandler(
    translation_service=translation_service,
    stadburo_service=stadburo_service,
    stadburo_keyboards=stadburo_keyboards,
    navigator_keyboards=navigator_keyboards
)

donations_handler = DonationsHandler(
    translation_service=translation_service,
    navigator_keyboards=navigator_keyboards
)

links_handler = LinksHandler(
    translation_service=translation_service,
    links_keyboards=links_keyboards
)

logs_handler = LogsHandler()




