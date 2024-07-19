from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery

from application.services.translation_service import TranslationService
from application.telegram.keyboards.canteens_keyboards import CanteensKeyboardsBuilder


class CanteensHandler:
    def __init__(self, translation_service: TranslationService, canteens_keyboards: CanteensKeyboardsBuilder):
        self.translation_service = translation_service
        self.canteens_keyboards = canteens_keyboards

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        self.__register_callbacks(router)
        return router

    def __register_handlers(self, router: Router):
        pass

    def __register_callbacks(self, router: Router):
        router.callback_query.register(self.menu_canteens_handler, F.data == "menu_canteens")
        router.callback_query.register(self.canteens_handler, F.data.startswith('canteen'))

    async def menu_canteens_handler(self, call: CallbackQuery, locale: str = 'ru'):
        # auxiliary.is_in_db(call)

        await call.message.edit_text(
            self.translation_service.translate(message_id='menu-canteens', locale=locale),
            reply_markup=self.canteens_keyboards.get_canteens(locale=locale)
        )
        # await call.message.edit_text("Еда\n\nВыберите столовую, чтобы получить меню.", reply_markup=inline.canteens)

    async def canteens_handler(self, call: CallbackQuery, locale: str = 'ru'):
        # func_name = f"{call.data[8:]}_handler"
        # set_func_and_person(func_name, tag, call.message)

        canteen = call.data[8:]

        # TODO переделать вывод описания столовых
        # if canteen == "colibri":
        #     data = (self.translation_service.translate(message_id='colibri-open-time', locale=locale) + '\n'
        #             + auxiliary.get_canteen_description('colibri'))
        #     await send_canteens_menu_handler(call, 'CoLibri', data, l10n)

        # else:
        canteen_name = ""
        match canteen:
            case "mensa_erlenring":
                canteen_name = "Mensa Erlenring"
            case "mensa_lahnberge":
                canteen_name = "Mensa Lahnberge"
            case "bistro":
                canteen_name = "Bistro"
            case "thm":
                canteen_name = "THM"
            case "cafeteria_lahnberge":
                canteen_name = "Cafeteria Lahnberge"
            case "mo_diner":
                canteen_name = "Mo's Dinner"

        # TODO переделать на апи получение меню столовых
        # if canteen == "thm":
        #     canteens_parser = thm_mensa_class.THMCanteenParser()
        #     data = canteens_parser.get_menu_from_canteen(canteen, l10n)
        #
        # else:
        #     canteens_parser = marburg_mensa_class.CanteensParser()
        #     data = canteens_parser.get_menu_from_canteen(canteen, l10n)
        #
        # await send_canteens_menu_handler(call, canteen_name, data, l10n)

    # TODO переделать вывод меню столовых
    async def send_canteens_menu_handler(self, call: CallbackQuery, canteen_name: str, data, locale: str = 'ru'):
        """Функция проверки, изменилось ли сообщение"""

        text = call.message.text
        first_line = text[:text.find('\n')]
        if canteen_name not in first_line:
            await call.message.edit_text(data, reply_markup=inline.get_canteens(l10n))
        await call.answer()
