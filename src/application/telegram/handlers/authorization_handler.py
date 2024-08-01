from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.filters import CommandStart, Command

from application.services.users_service import UsersService


class AuthorizationHandler:
    def __init__(self,
                 users_service: UsersService,
                 ):
        self.users_service = users_service

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        router.message(CommandStart)(self.start_authorization)

    def __register_callbacks(self, router: Router):
        pass
        # router.callback_query.register(self.menu_canteens_handler, F.data == "menu_canteens")
        # router.callback_query.register(self.canteens_handler, F.data.startswith('canteen'))

    async def start_authorization(self, message: Message, state: FSMContext, locale: str):

        user_id = message.chat.id
        print(await self.users_service.check_existence(user_id=user_id))
        if not await self.users_service.check_existence(user_id=user_id):
            print('Пользователя не существует')
        else:
            print('Пользователь существует')
        """
        1. Проверка что пользователь зарегестрирован
            1. Если пользователь не зарегестрирован, то добавлять в бд
            2. Если пользователь зарегестрирован, то отправлять сообщение пользователю 
               что тот уже зареган и предлагать открыть главное меню
        2. Отправлять сообщение админу о добавлении пользователя
        3. Предложить пользователю выбрать язык
        4. Предложить пользователю выбрать столовую
        """
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

