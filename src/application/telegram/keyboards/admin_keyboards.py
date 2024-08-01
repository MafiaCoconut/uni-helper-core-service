from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from application.services.translation_service import TranslationService


class AdminKeyboardsBuilder:
    def __init__(self,
                 translation_service: TranslationService,
                 ):
        self.translation_service = translation_service

    async def get_link_to_person(self, user_id: int):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Перейти на акк человека", url=f'tg://user?id={user_id}')]
            ]
        )
        go_to = await self.go_to('users')
        keyboard.inline_keyboard.append([*go_to.inline_keyboard[0]])
        return keyboard

    async def go_to(self, where: str):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад",
                                      callback_data=f"admin_menu {where}"),
                 InlineKeyboardButton(text="В главное меню",
                                      callback_data="admin_menu help")]
            ]
        )
        return keyboard

