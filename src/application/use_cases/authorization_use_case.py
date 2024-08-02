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
        # await self.web_interface.create_user(user=user)
        await self.telegram_interface.send_message(
            user_id=user.user_id,
            message=await self.translation_service.translate(message_id='welcome-message', locale=user.locale),
            keyboard=await self.authorization_keyboards.get_languages_list_from_start(locale=user.locale),
        )
        await self.admins_service.send_message_to_admin_about_new_user(user=user)


    async def start_canteen_config(self, menu_authorization_message_id: int, user: User):
        await self.telegram_interface.delete_keyboard(chat_id=user.user_id, message_id=menu_authorization_message_id)

        await self.telegram_interface.send_message(
            user_id=user.user_id,
            message=await self.translation_service.translate(message_id='choose-canteen-for-mailing', locale=user.locale),
            keyboard=await self.authorization_keyboards.get_canteens_list_to_change(locale=user.locale),
        )

    async def refresh_menu_authorization(self, callback, user: User):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message=await self.translation_service.translate(message_id='welcome-message', locale=user.locale),
            keyboard=await self.authorization_keyboards.get_languages_list_from_start(locale=user.locale)
        )

    async def user_already_exist(self, user: User):
        await self.telegram_interface.send_message(
            user_id=user.user_id,
            message=await self.translation_service.translate(message_id='reactivating-the-bot', locale=user.locale),
            keyboard=await self.authorization_keyboards.send_main_menu(locale=user.locale)
        )

        # await message.answer(await self.translation_service.translate(message_id='reactivating-the-bot', locale=locale))

    async def check_canteen(self, callback, user: User, canteen_id: int):
        if canteen_id == 0:
            pass
        else:
            canteen = await self.web_interface.get_canteens_info(canteen_id=canteen_id)

            await self.telegram_interface.edit_message_with_callback(
                callback=callback,
                message=await self.translation_service.translate(
                    message_id='is-sure-to-save-canteen', locale=user.locale, canteen=canteen.name
                ),
                keyboard=await self.authorization_keyboards.get_check_status_change_canteen(
                    canteen_id=canteen.canteen_id, locale=user.locale
                )

            )

    async def set_canteen(self, user: User, canteen_id: int):
        await self.web_interface.update_user_data(user_id=user.user_id, new_canteen_id=int(canteen_id))

        await self.telegram_interface.send_message(
            user_id=user.user_id,
            message=await self.translation_service.translate(message_id='menu_main', locale=user.locale),
        )


"""
1. Проверка что пользователь зарегестрирован + 
    1. Если пользователь не зарегестрирован, то добавлять в бд + 
    2. Если пользователь зарегестрирован, то отправлять сообщение пользователю + 
       что тот уже зареган и предлагать открыть главное меню
2. Отправлять сообщение админу о добавлении пользователя + 
3. Предложить пользователю выбрать язык +
4. Предложить пользователю выбрать столовую 
"""