import logging
from application.interfaces.telegram_interface import TelegramInterface
from application.services.settings_service import SettingsService
from application.services.users_service import UsersService
from infrastructure.config.logs_config import log_decorator, user_logger

error_logger = logging.getLogger('error_logger')
system_logger = logging.getLogger('system_logger')


class SendAdminsMailingTextUseCase:
    def __init__(
            self,
            users_service: UsersService,
            telegram_interface: TelegramInterface,
            settings_service: SettingsService,
    ):
        self.users_service = users_service
        self.telegram_interface = telegram_interface
        self.settings_service = settings_service

    @log_decorator(print_args=False)
    async def execute(self, mailing_text: str):
        users = await self.users_service.get_users()

        for user in users:
            if user.status == 'active':
                try:
                    await self.telegram_interface.send_message(
                        user_id=user.user_id,
                        message=mailing_text,
                    )
                except Exception as e:
                    error_logger.error(f"The menu could not be sent to the could not be sent. Error: {e}")
                    system_logger.error(f"The menu could not be sent to the user {user.id}. Error: {e}")
                    await self.settings_service.disable_user(user_id=user.user_id)













