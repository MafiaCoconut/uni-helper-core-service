from application.services.canteens_service import CanteensService
from infrastructure.config.interfaces_config import web_interface
from src.application.services.translation_service import TranslationService

translation_service = TranslationService()

canteens_service = CanteensService(web_interface=web_interface)


