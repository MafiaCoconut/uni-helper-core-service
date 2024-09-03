from sqlalchemy.testing.suite.test_reflection import users

from application.services.admin_service import AdminsService
from application.services.authorization_service import AuthorizationService
from application.services.canteens_service import CanteensService
from application.services.mailing_service import MailingService
from application.services.notification_service import NotificationService
from application.services.s3_service import S3Service
from application.services.scheduler_service import SchedulerService
from application.services.settings_service import SettingsService
from application.services.stadburo_service import StadburoService
from application.services.users_service import UsersService
from application.services.translation_service import TranslationService
from infrastructure.config.gateways_config import canteens_gateway, users_gateway, stadburo_gateway, \
    notification_gateway

from infrastructure.config.interfaces_config import telegram_interface, excel_interface
from infrastructure.config.keyboards_config import settings_keyboards, authorization_keyboards, admin_keyboards, \
    admin_menu_keyboards, menu_main_keyboards
from infrastructure.config.providers_config import keyboards_provider
from infrastructure.config.redis_config import redis_service
from infrastructure.config.s3_config import s3client
from infrastructure.config.scheduler_interfaces_config import get_scheduler_interface
from infrastructure.config.translation_config import translation_service

users_service = UsersService(
    users_gateway=users_gateway
)

notification_service = NotificationService(
    notification_gateway=notification_gateway,
)

canteens_service = CanteensService(
    canteens_gateway=canteens_gateway,
    telegram_interface=telegram_interface,
    translation_service=translation_service,
)

stadburo_service = StadburoService(
    stadburo_gateway=stadburo_gateway,
    translation_service=translation_service
)

settings_service = SettingsService(
    users_service=users_service,
    redis_service=redis_service,
    canteens_service=canteens_service,
    settings_keyboards=settings_keyboards,
    notification_service=notification_service,
    telegram_interface=telegram_interface,
)

admins_service = AdminsService(
    admin_keyboards=admin_keyboards,
    admin_menu_keyboards=admin_menu_keyboards,
    telegram_interface=telegram_interface,
    excel_interface=excel_interface,
    users_service=users_service,
    canteens_service=canteens_service,
    stadburo_service=stadburo_service,
    settings_service=settings_service,
)

s3_service = S3Service(
    s3client=s3client
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
    menu_main_keyboards=menu_main_keyboards
)


async def get_mailing_service() -> MailingService:
    return MailingService(
        redis_service=redis_service,
        users_service=users_service,
        canteens_service=canteens_service,
        settings_service=settings_service,
        telegram_interface=telegram_interface,
        translation_service=translation_service,
    )


def get_scheduler_service() -> SchedulerService:
    return SchedulerService(
        scheduler_interface=get_scheduler_interface(),
        s3_service=s3_service
    )
