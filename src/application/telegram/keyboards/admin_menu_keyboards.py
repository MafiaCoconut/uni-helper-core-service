from application.services.translation_service import TranslationService
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class AdminMenuKeyboardsBuilder:
    def __init__(self,
                 # translation_service: TranslationService
                 ):
        # self.translation_service = translation_service
        pass

    async def menu_main(self):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Пользователи", callback_data="admin_menu_users")],
                [InlineKeyboardButton(text="Столовые", callback_data="admin_menu_canteens")],
                [InlineKeyboardButton(text="Stadburo", callback_data="admin_menu_stadburo")],
                [InlineKeyboardButton(text="Логи", callback_data="admin_menu_logs")],
                [InlineKeyboardButton(text="Рассылка", callback_data="admin_menu_mailing")],
            ]
        )
        return keyboard

    async def menu_users(self):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Список пользователей", callback_data="admin_get_all_persons")],
                [InlineKeyboardButton(text="username, time, created", callback_data="admin_get_username_time_created")],
                [InlineKeyboardButton(text="id, username, time", callback_data="admin_get_id_username_time")],
                [InlineKeyboardButton(text="Изменить параметры", callback_data="admin_change_persons_parameters")],
                [InlineKeyboardButton(text="Количество пользователей", callback_data="admin_get_count_users")],
                [InlineKeyboardButton(text="Получить ссылку на пользователя", callback_data="admin_get_person_by_id")],
                [InlineKeyboardButton(text="Удалить пользователя", callback_data="admin_delete_person")],

                [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu_help")],
            ]
        )
        return keyboard

    async def menu_canteens(self):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Запуск парсера всех",
                                      callback_data="admin_start_canteen_parser_marburg all")],

                [InlineKeyboardButton(text="Erlenring парсер",
                                      callback_data="admin_start_canteen_parser_marburg mensa_erlenring"),
                 InlineKeyboardButton(text="меню", callback_data="admin_get_canteen_marburg mensa_erlenring")],

                [InlineKeyboardButton(text="Lahnberge парсер",
                                      callback_data="admin_start_canteen_parser_marburg mensa_lahnberge"),
                 InlineKeyboardButton(text="меню", callback_data="admin_get_canteen_marburg mensa_lahnberge")],

                [InlineKeyboardButton(text="Bistro парсер", callback_data="admin_start_canteen_parser_marburg bistro"),
                 InlineKeyboardButton(text="меню", callback_data="admin_get_canteen_marburg bistro")],

                [InlineKeyboardButton(text="THM", callback_data="admin_start_canteen_parser_giessen thm"),
                 InlineKeyboardButton(text="меню", callback_data="admin_get_canteen_giessen thm")],

                # [InlineKeyboardButton(text="Cafeteria парсер",
                #                       callback_data="admin_start_canteen_parser_marburg cafeteria_lahnberge"),
                #  InlineKeyboardButton(text="меню", callback_data="admin_get_canteen_marburg cafeteria_lahnberge")],

                # [InlineKeyboardButton(text="Mo diner парсер",
                #                       callback_data="admin_start_canteen_parser_marburg mo_diner"),
                #  InlineKeyboardButton(text="меню", callback_data="admin_get_canteen_marburg mo_diner")],

                [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu_help")],

            ]
        )
        return keyboard

    async def menu_stadburo(self):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Запустить парсер", callback_data="admin_start_termins_parser")],

                [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu_help")],

            ]
        )
        return keyboard

    async def menu_logs(self):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Прислать логи", callback_data="admin_send_logs")],
                [InlineKeyboardButton(text="Очистить логи", callback_data="admin_clear_logs")],

                [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu_help")],

            ]
        )
        return keyboard

    async def menu_mailing(self):
        pass




