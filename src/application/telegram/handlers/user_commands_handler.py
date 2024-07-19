from application.services.translation_service import TranslationService

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext


class UserCommandsHandler:
    def __init__(self, translation_service: TranslationService):
        self.translation_service = translation_service

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        return router

    def __register_handlers(self, router: Router):
        router.message(CommandStart())(self.command_start_handler)
        router.message(Command("main_menu"))(self.command_main_menu_handler)

    async def command_start_handler(self, message: Message, state: FSMContext) -> None:

        # TODO переделать в сервис регистрации
        pass
        # if not await state.get_data():
        #     telegram_id = message.chat.id
        #     username = message.from_user.username
        #
        #     language = message.from_user.language_code
        #     if language not in list_of_available_languages:
        #         language = 'en'
        #
        #     l10n = auxiliary.get_l10n(language)
        #
        #     if not user_is_exists(telegram_id) or str(telegram_id) == os.getenv("ADMINS_ID"):
        #         save_user(telegram_id=telegram_id, username=username, language=language)
        #
        #         user_logger = logging.getLogger('user_logging')
        #         user_logger.info(f"Add User: {username}/{telegram_id} Language[{message.from_user.language_code}]")
        #
        #         await auxiliary.send_message_to_admin(f"Добавлен пользователь:\n\n"
        #                                               f"id: {telegram_id}\n"
        #                                               f"username: @{username}\n"
        #                                               f"language: {message.from_user.language_code}",
        #                                               _reply_markup=inline_admin.get_person_by_id(telegram_id))
        #
        #         menu_message = await message.answer(l10n.format_value('welcome-message'),
        #                                             reply_markup=inline.get_settings_language_from_start(l10n,
        #                                                                                                  'from_start'))
        #         await state.set_state(GetStartMenu.start_menu_id)
        #         await state.update_data(start_menu_id=menu_message.message_id)
        #
        #         # await message.answer("Выберите столовую, рассылку которой хотите получать",
        #         #                      reply_markup=inline.get_change_canteen())
        #
        #     else:
        #         await message.answer(l10n.format_value('reactivating-the-bot'), reply_markup=inline.get_main_menu(l10n))

    async def command_main_menu_handler(self, message: Message, state: FSMContext) -> None:
        if not await state.get_data():
            await message.answer(self.translation_service.translate('menu-main', locale='en'),
                                 # reply_markup=inline.get_main_menu(l10n)
            )


