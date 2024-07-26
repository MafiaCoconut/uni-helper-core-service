from application.services.canteens_service import CanteensService
from application.services.stadburo_service import StadburoService
from infrastructure.config.interfaces_config import web_interface, telegram_interface
from application.services.translation_service import TranslationService

translation_service = TranslationService()

canteens_service = CanteensService(
    web_interface=web_interface,
    telegram_interface=telegram_interface,
    translation_service=translation_service
)
stadburo_service = StadburoService(web_interface=web_interface)


