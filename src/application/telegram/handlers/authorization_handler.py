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
        router.callback_query.register(self.authorization_locale_config, F.data.startswith("authorization_locales_config"))

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
            await self.authorization_service.user_already_exist(user=User(user_id=user_id, locale=locale))

    async def authorization_locale_config(self, callback: CallbackQuery, state: FSMContext, locale: str):
        new_locale = callback.data[callback.data.rfind(' ') + 1:]

        user = User(
            user_id=callback.message.chat.id,
            locale=new_locale
        )

        await self.authorization_service.set_new_locale(user_id=callback.message.chat.id, new_locale=new_locale)
        await callback.answer()

        await self.authorization_service.refresh_menu_authorization(callback=callback, user=user)



    async def authorization_canteen_config(self, callback: CallbackQuery, state: FSMContext, locale: str):

        pass
        # await self.authorization_service.start_canteen_config(user=user, menu_authorization_message_id=)


