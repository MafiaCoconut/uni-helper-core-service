from application.services.translation_service import TranslationService
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


class NavigatorKeyboardsBuilder:
    def __init__(self, translation_service: TranslationService):
        self.translation_service = translation_service

    async def get_go_to(self, locale: str, where: str):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=await self.translation_service.translate(message_id='back', locale=locale),
                        callback_data=f"menu_{where}"),
                    InlineKeyboardButton(
                        text=await self.translation_service.translate(message_id='to-menu-main', locale=locale),
                        callback_data="menu_main")
                ]
            ]
        )
        return keyboard

    async def get_go_to_menu_main(self, locale: str):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='to-menu-main', locale=locale),
                    callback_data="menu_main")]
            ]
        )
        return keyboard

    async def get_send_menu_main(self, locale: str):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='open-menu-main', locale=locale),
                    callback_data='send_menu_main')]
            ]
        )
        return keyboard
