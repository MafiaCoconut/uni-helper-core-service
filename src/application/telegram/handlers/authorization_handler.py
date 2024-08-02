from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.filters import CommandStart, Command
from icecream import ic

from application.providers.keyboards_provider import KeyboardsProvider
from application.services.authorization_service import AuthorizationService
from application.services.translation_service import TranslationService
from application.services.users_service import UsersService
from application.telegram.keyboards.authorization_keyboards import AuthorizationKeyboardsBuilder
from domain.entities.user import User


class AuthorizationHandler:
    def __init__(self,
                 users_service: UsersService,
                 translation_service: TranslationService,
                 authorization_service: AuthorizationService,
                 ):
        self.users_service = users_service
        self.translation_service = translation_service
        self.authorization_service = authorization_service

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        router.message(Command('start'))(self.start_authorization)

    def __register_callbacks(self, router: Router):
        pass
        # router.callback_query.register(self.menu_canteens_handler, F.data == "menu_canteens")
        # router.callback_query.register(self.canteens_handler, F.data.startswith('canteen'))

    async def start_authorization(self, message: Message, state: FSMContext, locale: str):
        user_id = message.chat.id

        # if not await self.users_service.check_existence(user_id=user_id):
        if await self.users_service.check_existence(user_id=user_id):
            users_language = message.from_user.language_code
            users_username = message.from_user.username
            users_name = message.from_user.first_name + " " + (
                message.from_user.last_name if message.from_user.last_name is not None else ""
            )

            user = User(
                user_id=user_id,
                username=users_username if users_username is not None else "-",
                name=users_name if users_name is not None else "-",
                mailing_time="11:45",
                locale=users_language if users_language in await self.translation_service.get_list_of_languages() else 'en',
            )
            await state.update_data(user=user)

            await self.authorization_service.start_authorization(user=user)

        else:
            #TODO перенести эту часть в сервис
            await message.answer(await self.translation_service.translate(message_id='reactivating-the-bot', locale=locale))

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

