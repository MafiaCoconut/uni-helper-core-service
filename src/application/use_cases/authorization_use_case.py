from icecream import ic

from application.interfaces.telegram_interface import TelegramInterface
from application.services.admin_service import AdminsService
from application.services.canteens_service import CanteensService
from application.services.notification_service import NotificationService
from application.services.translation_service import TranslationService
from application.services.users_service import UsersService
from application.telegram.keyboards.authorization_keyboards import AuthorizationKeyboardsBuilder
from application.telegram.keyboards.menu_main_keyboards import MenuMainKeyboardsBuilder
from domain.entities.user import User
from infrastructure.config.logs_config import log_decorator


class AuthorizationUseCase:
    def __init__(self,
                 # web_interface: WebInterface,
                 users_service: UsersService,
                 canteens_service: CanteensService,
                 telegram_interface: TelegramInterface,
                 notification_service: NotificationService,
                 admins_service: AdminsService,
                 translation_service: TranslationService,
                 authorization_keyboards: AuthorizationKeyboardsBuilder,
                 menu_main_keyboards: MenuMainKeyboardsBuilder,
                 ):
        self.telegram_interface = telegram_interface

        self.users_service = users_service
        self.canteens_service = canteens_service
        self.notification_service = notification_service
        self.admins_service = admins_service
        self.translation_service = translation_service

        self.authorization_keyboards = authorization_keyboards
        self.menu_main_keyboards = menu_main_keyboards

    @log_decorator(print_args=False)
    async def start_authorization(self,
                                  user_id: int, name: str = "-",
                                  username: str = "-", locale: str = "en"
                                  ) -> int:
        user = User(
                user_id=user_id,
                name=name,
                username=username,
                locale=locale,
                mailing_time="-",
                canteen_id="0",
                status="active",
            )
        await self.users_service.create_user(user=user)
        message_id = await self.telegram_interface.send_message(
            user_id=user_id,
            message=await self.translation_service.translate(message_id='welcome-message', locale=locale),
            keyboard=await self.authorization_keyboards.get_languages_list_from_start(locale=locale),
        )
        await self.admins_service.send_message_to_admin_about_new_user(user=user)

        return message_id

    @log_decorator(print_args=False)
    async def start_canteen_config(self, menu_authorization_message_id: int, user: User) -> int:
        try:
            await self.telegram_interface.delete_keyboard(chat_id=user.user_id,
                                                          message_id=menu_authorization_message_id)
        except:
            pass

        message_id = await self.telegram_interface.send_message(
            user_id=user.user_id,
            message=await self.translation_service.translate(message_id='choose-canteen-for-mailing',
                                                             locale=user.locale),
            keyboard=await self.authorization_keyboards.get_canteens_list_to_change(locale=user.locale),
        )
        return message_id

    @log_decorator(print_args=False, print_kwargs=False)
    async def refresh_menu_authorization(self, callback, user: User):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message=await self.translation_service.translate(message_id='welcome-message', locale=user.locale),
            keyboard=await self.authorization_keyboards.get_languages_list_from_start(locale=user.locale)
        )

    @log_decorator(print_args=False, print_kwargs=False)
    async def user_already_exist(self, user: User) -> int:
        message_id = await self.telegram_interface.send_message(
            user_id=user.user_id,
            message=await self.translation_service.translate(message_id='reactivating-the-bot', locale=user.locale),
            keyboard=await self.authorization_keyboards.send_main_menu(locale=user.locale)
        )
        return message_id

        # await message.answer(await self.translation_service.translate(message_id='reactivating-the-bot', locale=locale))

    @log_decorator(print_args=False, print_kwargs=False)
    async def check_canteen(self, callback, user: User, canteen_id: int):
        if canteen_id == 0:
            await self.telegram_interface.edit_message_with_callback(
                callback=callback,
                message=await self.translation_service.translate(
                    message_id="null-canteen-has-been-selected", locale=user.locale
                ),
                keyboard=await self.menu_main_keyboards.get_menu_main(locale=user.locale)
            )
        else:
            canteen = await self.canteens_service.get_canteens_info(canteen_id=canteen_id)
            await self.telegram_interface.edit_message_with_callback(
                callback=callback,
                message=await self.translation_service.translate(
                    message_id='is-sure-to-save-canteen', locale=user.locale, canteen=canteen.name
                ),
                keyboard=await self.authorization_keyboards.get_check_status_change_canteen(
                    canteen_id=canteen.canteen_id, locale=user.locale
                )

            )

    @log_decorator(print_args=False, print_kwargs=False)
    async def set_canteen(self, user: User, canteen_id: int, canteens_config_message_id: int) -> int:
        await self.telegram_interface.delete_message(chat_id=user.user_id, message_id=canteens_config_message_id)
        await self.users_service.update_user(
            user_id=user.user_id,
            new_canteen_id=int(canteen_id),
            new_mailing_time="11:45",
        )
        await self.notification_service.set_canteens_menu_mailing(user_id=user.user_id, mailing_time="11:45")

        message_id = await self.telegram_interface.send_message(
            user_id=user.user_id,
            message=await self.translation_service.translate(message_id='menu-main', locale=user.locale),
            keyboard=await self.menu_main_keyboards.get_menu_main(locale=user.locale)
        )
        return message_id
