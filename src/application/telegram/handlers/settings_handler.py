from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from application.services.settings_service import SettingsService
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder


class SettingsHandler:
    def __init__(self,
                 settings_service: SettingsService,
                 settings_keyboards: SettingsKeyboardsBuilder
                 ):
        self.settings_service = settings_service
        self.settings_keyboards = settings_keyboards

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        pass

    def __register_callbacks(self, router: Router):
        router.callback_query.register(self.set_new_locale, F.data.startswith('settings_language'))

    async def set_new_locale(self, callback: CallbackQuery, state: FSMContext, locale: str):
        data = await state.get_data()
        user = data.get('user')

        new_locale = callback.data[callback.data.rfind('_')+1:]
        print(new_locale)
        user.locale = new_locale
        await state.update_data(user=user)

        where_was_called = callback.data[callback.data.find(' ')+1:callback.data.rfind('_')]
        print(where_was_called)

        await self.settings_service.set_new_locale(user_id=callback.message.chat.id, new_locale=new_locale)
        await callback.answer()

        await self.settings_service.send_menu_where_was_called(
            callback=callback, where_was_called=where_was_called, user=user
        )

