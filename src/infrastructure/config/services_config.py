from application.services.admin_service import AdminsService
from application.services.authorization_service import AuthorizationService
from application.services.canteens_service import CanteensService
from application.services.notification_service import NotificationService
from application.services.settings_service import SettingsService
from application.services.stadburo_service import StadburoService
from application.services.users_service import UsersService
from application.services.translation_service import TranslationService
from infrastructure.config.gateways_config import canteens_gateway, users_gateway, stadburo_gateway, \
    notification_gateway

from infrastructure.config.interfaces_config import telegram_interface
from infrastructure.config.keyboards_config import settings_keyboards, authorization_keyboards, admin_keyboards, \
    admin_menu_keyboards
from infrastructure.config.providers_config import keyboards_provider
from infrastructure.config.redis_config import redis_service
from infrastructure.config.translation_config import translation_service

canteens_service = CanteensService(
    users_gateway=users_gateway,
    canteens_gateway=canteens_gateway,
    telegram_interface=telegram_interface,
    translation_service=translation_service
)
stadburo_service = StadburoService(
    stadburo_gateway=stadburo_gateway,
    translation_service=translation_service
)

users_service = UsersService(
    users_gateway=users_gateway
)

admins_service = AdminsService(
    admin_keyboards=admin_keyboards,
    admin_menu_keyboards=admin_menu_keyboards,
    telegram_interface=telegram_interface,
    users_gateway=users_gateway,
    canteens_gateway=canteens_gateway,
    stadburo_gateway=stadburo_gateway,
)

notification_service = NotificationService(
    notification_gateway=notification_gateway
)

settings_service = SettingsService(
    users_service=users_service,
    redis_service=redis_service,
    canteens_service=canteens_service,
    settings_keyboards=settings_keyboards,
    notification_service=notification_service,
    telegram_interface=telegram_interface,
)

authorization_service = AuthorizationService(
    users_service=users_service,
    canteens_service=canteens_service,
    telegram_interface=telegram_interface,
    admins_service=admins_service,
    notification_service=notification_service,
    settings_service=settings_service,
    authorization_keyboards=authorization_keyboards,
    translation_service=translation_service,
)




