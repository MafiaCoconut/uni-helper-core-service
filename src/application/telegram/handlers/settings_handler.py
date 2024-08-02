from aiogram import Router, F
from aiogram.types import CallbackQuery

from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder


class SettingsHandler:
    def __init__(self,
                 settings_keyboards: SettingsKeyboardsBuilder
                 ):
        self.settings_keyboards = settings_keyboards

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        pass

    def __register_callbacks(self, router: Router):
        router.callback_query.register(self.set_new_locale, F.data.starswith('settings_language'))
        # router.callback_query.register(self.menu_canteens_handler, F.data == "menu_canteens")
        # router.callback_query.register(self.canteens_handler, F.data.startswith('canteen'))

    def set_new_locale(self, callback: CallbackQuery, locale: str):
        new_locale = callback.data[callback.data.rfind('_')+1:]
        print(new_locale)
