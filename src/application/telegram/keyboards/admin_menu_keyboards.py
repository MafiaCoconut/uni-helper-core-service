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
                [InlineKeyboardButton(text="Пользователи", callback_data="admin_menu users")],
                [InlineKeyboardButton(text="Столовые", callback_data="admin_menu canteens")],
                [InlineKeyboardButton(text="Stadburo", callback_data="admin_menu stadburo")],
                [InlineKeyboardButton(text="Логи", callback_data="admin_menu logs")],
                [InlineKeyboardButton(text="Рассылка", callback_data="admin_menu mailing")],
            ]
        )
        return keyboard

    async def menu_users(self):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Список пользователей", callback_data="admin_get_all_users")],
                [InlineKeyboardButton(text="Количество пользователей", callback_data="admin_get_count_users")],
                [InlineKeyboardButton(text="Получить ссылку на пользователя", callback_data="admin_get_person_by_id")],
                # [InlineKeyboardButton(text="Удалить пользователя", callback_data="admin_delete_person")],
                # [InlineKeyboardButton(text="username, time, created", callback_data="admin_get_username_time_created")],
                # [InlineKeyboardButton(text="id, username, time", callback_data="admin_get_id_username_time")],
                # [InlineKeyboardButton(text="Изменить параметры", callback_data="admin_change_persons_parameters")],

                [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu help")],
            ]
        )
        return keyboard

    async def menu_canteens(self):
        menu = "Info"
        on_off = "On/Off"
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Запуск парсера всех",
                                      callback_data="admin_start_canteen_parser_all")],

                [
                    InlineKeyboardButton(text="Erlenring парсер", callback_data="admin_start_canteen_parser 1"),
                    InlineKeyboardButton(text=menu, callback_data="admin_get_canteen 1"),
                    InlineKeyboardButton(text=on_off, callback_data="admin_change_canteen_status 1")
                ],

                [
                    InlineKeyboardButton(text="Lahnberge парсер", callback_data="admin_start_canteen_parser 2"),
                    InlineKeyboardButton(text=menu, callback_data="admin_get_canteen 2"),
                    InlineKeyboardButton(text=on_off, callback_data="admin_change_canteen_status 2")
                ],

                [
                    InlineKeyboardButton(text="Bistro парсер", callback_data="admin_start_canteen_parser 3"),
                    InlineKeyboardButton(text=menu, callback_data="admin_get_canteen 3"),
                    InlineKeyboardButton(text=on_off, callback_data="admin_change_canteen_status 3")
                ],

                [
                    InlineKeyboardButton(text="THM", callback_data="admin_start_canteen_parser 6"),
                    InlineKeyboardButton(text=menu, callback_data="admin_get_canteen 6"),
                    InlineKeyboardButton(text=on_off, callback_data="admin_change_canteen_status 6")
                ],

                [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu help")],

            ]
        )
        return keyboard

    async def menu_stadburo(self):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Запустить парсер", callback_data="admin_start_termins_parser")],

                [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu help")],

            ]
        )
        return keyboard

    async def menu_logs(self):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Прислать логи", callback_data="admin_send_logs")],
                [InlineKeyboardButton(text="Очистить логи", callback_data="admin_clear_logs")],

                [InlineKeyboardButton(text="В главное меню", callback_data="admin_menu help")],

            ]
        )
        return keyboard

    async def menu_mailing(self):
        pass
