from application.services.admin_service import AdminsService
from application.services.authorization_service import AuthorizationService
from application.services.canteens_service import CanteensService
from application.services.stadburo_service import StadburoService
from application.services.users_service import UsersService
from application.services.translation_service import TranslationService

from infrastructure.config.interfaces_config import web_interface, telegram_interface
from infrastructure.config.providers_config import keyboards_provider
from infrastructure.config.translation_config import translation_service

canteens_service = CanteensService(
    web_interface=web_interface,
    telegram_interface=telegram_interface,
    translation_service=translation_service
)
stadburo_service = StadburoService(
    web_interface=web_interface,
    translation_service=translation_service
)

users_service = UsersService(
    web_interface=web_interface
)

admins_service = AdminsService(
    keyboards_provider=keyboards_provider,
    telegram_interface=telegram_interface
)

authorization_service = AuthorizationService(
    web_interface=web_interface,
    telegram_interface=telegram_interface,
    admins_service=admins_service,
    keyboards_provider=keyboards_provider,
    translation_service=translation_service,
)




