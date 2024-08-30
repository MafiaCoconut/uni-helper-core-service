from icecream import ic
from sqlalchemy.testing.plugin.plugin_base import logging

from application.interfaces.telegram_interface import TelegramInterface
from application.services.canteens_service import CanteensService
from application.services.translation_service import TranslationService
from application.services.users_service import UsersService
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from application.use_cases.settings_user_data_use_case import SettingsUserDataUseCase
from domain.entities.user import User
from infrastructure.config.logs_config import log_decorator

user_logger = logging.getLogger("user_logger")
error_logger = logging.getLogger("error_logger")


class SettingsUseCase:
    def __init__(self,
                 users_service: UsersService,
                 translation_service: TranslationService,
                 canteens_service: CanteensService,
                 telegram_interface: TelegramInterface,
                 settings_keyboards: SettingsKeyboardsBuilder,
                 update_user_data_use_case: SettingsUserDataUseCase,
                 ):
        self.users_service = users_service
        self.translation_service = translation_service
        self.canteens_service = canteens_service
        self.telegram_interface = telegram_interface
        self.settings_keyboards = settings_keyboards
        self.update_user_data_use_case = update_user_data_use_case

    @log_decorator(print_args=False)
    async def get_settings_text(self, user_id: int, locale: str):
        user = await self.users_service.get_user(user_id=user_id)
        ic(user)
        text = await self.translation_service.translate(message_id='menu-settings-heading', locale=locale) + '\n'
        if user.mailing_time != '-':
            text += await self.translation_service.translate(message_id='menu-settings-mailing-on', locale=locale) + '\n'
            text += await self.translation_service.translate(message_id='menu-settings-mailing-time', locale=locale,
                                                             mailing_time=user.mailing_time) + '\n'
            canteen = await self.canteens_service.get_canteens_info(canteen_id=user.canteen_id)
            text += await self.translation_service.translate(
                message_id='menu-settings-canteen', locale=locale,
                canteen=canteen.name + '\n'
            )
        else:
            text += await self.translation_service.translate(message_id='menu-settings-mailing-off', locale=locale) + '\n'

        text += '\n' + await self.translation_service.translate(message_id='menu-settings-ending', locale=locale)

        return text

    @log_decorator(print_args=False)
    async def menu_settings(self, callback, user_id: int, locale: str):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message=await self.get_settings_text(user_id=user_id, locale=locale),
            keyboard=await self.settings_keyboards.get_menu(locale=locale),
        )

    @log_decorator(print_args=False)
    async def change_locale(self, callback, user_id: int, new_locale: str):
        await self.update_user_data_use_case.update_locale(user_id=user_id, new_locale=new_locale)

        try:
            await self.menu_settings(callback, user_id=user_id, locale=new_locale)
        except Exception as e:
            ic(e)

        user_logger.info(
            message=f"User: {callback.message.chat.username}/{callback.message.chat.id} "
                    f"Changed Locale to {new_locale}"
        )

    @log_decorator(print_args=False)
    async def menu_change_mailing_time(self, callback, locale: str):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message=await self.translation_service.translate(
                message_id='enter-appropriate-time-for-your-daily-mailing',
                locale=locale,
            ),
            keyboard=await self.settings_keyboards.get_change_mailing_time(locale=locale)
        )

    @log_decorator(print_args=False)
    async def change_mailing_time(self, callback, user_id: int, new_mailing_time: str, locale: str):
        await self.update_user_data_use_case.update_mailing_time(user_id=user_id, new_mailing_time=new_mailing_time)
        try:
            await self.menu_settings(callback, user_id=user_id, locale=locale)
        except Exception as e:
            ic(e)

        user_logger.info(
            message=f"User: {callback.message.chat.username}/{callback.message.chat.id} "
                    f"Changed MailingTime to {new_mailing_time}"
        )


    @log_decorator(print_args=False)
    async def change_mailing_status(self, callback, user_id: int, locale: str):
        user = await self.users_service.get_user(user_id=user_id)
        ic(user)

        if user.mailing_time == '-':
            await self.update_user_data_use_case.enable_mailing(user_id=user_id, new_mailing_time='11:45')
            if user.canteen_id == 0:
                await self.update_user_data_use_case.update_canteen_id(user_id=user_id, new_canteen_id=1)
            user_logger.info(
                message=f"User: {callback.message.chat.username}/{callback.message.chat.id} "
                        f"Turn on the mailing"
            )
        else:
            await self.update_user_data_use_case.disable_mailing(user_id=user_id)
            user_logger.info(
                message=f"User: {callback.message.chat.username}/{callback.message.chat.id} "
                        f"Turn off the mailing"
            )

        try:
            await self.menu_settings(callback, user_id=user_id, locale=locale)
        except Exception as e:
            error_logger.error(message=e)

    @log_decorator(print_args=False)
    async def menu_change_canteen(self, callback, user_id: int, locale: str):
        await self.telegram_interface.edit_message_with_callback(
            callback=callback,
            message=await self.translation_service.translate(
                message_id='choose-canteen-for-mailing', locale=locale
            ),
            keyboard=await self.settings_keyboards.get_canteens_list_to_change(locale=locale),
        )

    @log_decorator(print_args=False)
    async def change_canteen(self, callback, user_id: int, new_canteen_id: int, locale: str):
        await self.update_user_data_use_case.update_canteen_id(new_canteen_id=new_canteen_id, user_id=user_id)

        try:
            await self.menu_settings(callback, user_id=user_id, locale=locale)
        except Exception as e:
            ic(e)

        user_logger.info(
            message=f"User: {callback.message.chat.username}/{callback.message.chat.id} "
                    f"Changed CanteenID to {new_canteen_id}"
        )
