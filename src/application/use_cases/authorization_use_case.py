from application.interfaces.telegram_interface import TelegramInterface
from application.interfaces.web_interface import WebInterface
from application.services.admin_service import AdminsService
from application.services.translation_service import TranslationService
from application.telegram.keyboards.authorization_keyboards import AuthorizationKeyboardsBuilder
from domain.entities.user import User


class AuthorizationUseCase:
    def __init__(self,
                 web_interface: WebInterface,
                 telegram_interface: TelegramInterface,
                 admins_service: AdminsService,
                 authorization_keyboards: AuthorizationKeyboardsBuilder,
                 translation_service: TranslationService,
                 ):
        self.web_interface = web_interface
        self.telegram_interface = telegram_interface
        self.admins_service = admins_service
        self.authorization_keyboards = authorization_keyboards
        self.translation_service = translation_service

    async def start_authorization(self, user: User):
        await self.web_interface.create_user(user=user)
        await self.admins_service.send_message_to_admin_about_new_user(user=user)
        await self.telegram_interface.send_message(
            user_id=user.user_id,
            message=await self.translation_service.translate(message_id='welcome-message', locale=user.locale),
            keyboard=await self.authorization_keyboards.get_languages_list_from_start(locale=user.locale),
        )

    async def state_set_canteen(self, user: User):
        await self.telegram_interface.send_message(
            user_id=user.user_id,
            message=await self.translation_service.translate(message_id='set-canteen-message', locale=user.locale),
            # keyboard=await self.authorization_keyboards.get_canteens_list(locale=user.locale)
        )

        """
        1. Проверка что пользователь зарегестрирован + 
            1. Если пользователь не зарегестрирован, то добавлять в бд
            2. Если пользователь зарегестрирован, то отправлять сообщение пользователю 
               что тот уже зареган и предлагать открыть главное меню
        2. Отправлять сообщение админу о добавлении пользователя + 
        3. Предложить пользователю выбрать язык 
        4. Предложить пользователю выбрать столовую 
        """
