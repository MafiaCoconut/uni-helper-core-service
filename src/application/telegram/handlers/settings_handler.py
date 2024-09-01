from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from icecream import ic

from application.services.settings_service import SettingsService
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from domain.entities.user import User


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
        router.callback_query.register(self.menu_settings_handler, F.data == "menu_settings")
        router.callback_query.register(self.change_locale_handler, F.data.startswith("settings_locales_config"))
        router.callback_query.register(self.menu_change_mailing_time_handler, F.data == "menu_settings_change_mailing_time")
        router.callback_query.register(self.change_mailing_time_handler, F.data.startswith("settings_change_mailing_time"))
        router.callback_query.register(self.change_mailing_status_handler, F.data == "change_status_mailing")

        router.callback_query.register(self.menu_change_canteen_handler, F.data == "change_canteen_from_settings")
        router.callback_query.register(self.change_canteen_handler, F.data.startswith("settings_canteen_change"))

        # router.callback_query.register(self.set_new_locale, F.data.startswith('settings_language'))
        # Настройки
        # router.callback_query.register(self.change_mailing_time_handler, F.data == "change_mailing_time")
        # router.callback_query.register(self.change_status_mailing_handler, F.data == 'change_status_mailing')
        # dp.callback_query.register(settings_callback.change_status_numbers_in_menu_handler,
        #                            F.data == 'change_status_numbers_in_menu')
        # router.callback_query.register(self.change_language_handler, F.data.startswith('settings_language'))
        # router.callback_query.register(self.set_canteen_to_person_status_question,
        #                            F.data.startswith('change_canteen'))
        # router.callback_query.register(self.set_canteen_to_person_status_check_handler,
        #                            F.data.startswith('settings_canteen_change'))
        # router.callback_query.register(self.set_canteen_to_person_status_save,
        #                            F.data.startswith('settings_canteen_yes'))

    async def menu_settings_handler(self, call: CallbackQuery, locale: str):
        await self.settings_service.menu_settings(callback=call, user_id=call.message.chat.id, locale=locale)
        # await call.answer()

    async def change_locale_handler(self, call: CallbackQuery, locale: str):
        new_locale = call.data[call.data.find(' ') + 1:]
        await self.settings_service.change_locale(callback=call, user_id=call.message.chat.id, new_locale=new_locale)
        # await call.answer()

    async def menu_change_mailing_time_handler(self, call: CallbackQuery, locale: str):
        await self.settings_service.menu_change_mailing_time(callback=call, locale=locale)
        # await call.answer()

    async def change_mailing_time_handler(self, call: CallbackQuery, locale: str):
        new_mailing_time = call.data[call.data.find(' ') + 1:]
        # ic(new_mailing_time)
        await self.settings_service.change_mailing_time(callback=call, user_id=call.message.chat.id,
                                                        locale=locale, new_mailing_time=new_mailing_time)
        # await call.answer()

    async def change_mailing_status_handler(self, call: CallbackQuery, locale: str):
        await self.settings_service.change_mailing_status(callback=call, user_id=call.message.chat.id, locale=locale)
        # await call.answer()

    async def menu_change_canteen_handler(self, call: CallbackQuery, locale: str):
        await self.settings_service.menu_change_canteen(callback=call, user_id=call.message.chat.id, locale=locale)
        # await call.answer()

    async def change_canteen_handler(self, call: CallbackQuery, locale: str):
        new_canteen_id = call.data[call.data.find(' ') + 1:]
        await self.settings_service.change_canteen(callback=call, user_id=call.message.chat.id,
                                                   locale=locale, new_canteen_id=new_canteen_id)
        # await call.answer()

    # async def set_new_locale(self, callback: CallbackQuery, state: FSMContext, locale: str):
    #     pass
    # new_locale = callback.data[callback.data.rfind('_') + 1:]
    # where_was_called = callback.data[callback.data.find(' ') + 1:callback.data.rfind('_')]
    # print(where_was_called)
    #
    # data = await state.get_data()
    # user = data.get('user')
    #
    # # TODO если при настройке кантины state будет не нужен, то можно убрать
    # if user is not None:
    #     user.locale = new_locale
    # else:
    #     user = User(
    #         user_id=callback.message.chat.id,
    #         locale=new_locale
    #     )
    # await state.update_data(user=user)
    #
    # await self.settings_service.set_new_locale(user_id=callback.message.chat.id, new_locale=new_locale)
    # await callback.answer()
    #
    # await self.settings_service.send_menu_where_was_called(
    #     callback=callback, where_was_called=where_was_called, user=user
    # )
