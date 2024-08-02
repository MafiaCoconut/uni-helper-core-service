from application.interfaces.telegram_interface import TelegramInterface
from application.interfaces.web_interface import WebInterface
from application.providers.keyboards_provider import KeyboardsProvider
from application.services.admin_service import AdminsService
from application.services.translation_service import TranslationService
from application.telegram.keyboards.authorization_keyboards import AuthorizationKeyboardsBuilder
from application.use_cases.authorization_use_case import AuthorizationUseCase
from domain.entities.user import User


class AuthorizationService:
    def __init__(self,
                 web_interface: WebInterface,
                 telegram_interface: TelegramInterface,
                 admins_service: AdminsService,
                 authorization_keyboards: AuthorizationKeyboardsBuilder,
                 translation_service: TranslationService,
                 ):
        # self.keyboards_provider = keyboards_provider

        self.authorization_use_case = AuthorizationUseCase(
            web_interface=web_interface,
            telegram_interface=telegram_interface,
            admins_service=admins_service,
            authorization_keyboards=authorization_keyboards,
            translation_service=translation_service
        )

    # @property
    # def authorization_keyboards(self):
    #     return self.keyboards_provider.get_authorization_keyboards()

    async def start_authorization(self, user: User):
        await self.authorization_use_case.start_authorization(user=user)
