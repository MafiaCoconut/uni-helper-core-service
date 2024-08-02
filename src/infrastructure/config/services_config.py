from application.services.admin_service import AdminsService
from application.services.authorization_service import AuthorizationService
from application.services.canteens_service import CanteensService
from application.services.settings_service import SettingsService
from application.services.stadburo_service import StadburoService
from application.services.users_service import UsersService
from application.services.translation_service import TranslationService

from infrastructure.config.interfaces_config import web_interface, telegram_interface
from infrastructure.config.keyboards_config import settings_keyboards, authorization_keyboards, admin_keyboards
from infrastructure.config.providers_config import keyboards_provider
from infrastructure.config.redis_config import redis_service
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
    admin_keyboards=admin_keyboards,
    telegram_interface=telegram_interface
)

authorization_service = AuthorizationService(
    web_interface=web_interface,
    telegram_interface=telegram_interface,
    admins_service=admins_service,
    authorization_keyboards=authorization_keyboards,
    translation_service=translation_service,
)


settings_service = SettingsService(
    users_service=users_service,
    redis_service=redis_service,
    authorization_service=authorization_service,
    settings_keyboards=settings_keyboards,

)




