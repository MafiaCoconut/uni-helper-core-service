from application.services.translation_service import TranslationService
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


class MenuMainKeyboardsBuilder:
    def __init__(self, translation_service: TranslationService):
        self.translation_service = translation_service

    async def get_menu_main(self, locale: str) -> InlineKeyboardMarkup:
        main_menu = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='main-menu-canteen', locale=locale),
                    callback_data="menu_canteens")],
                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='main-menu-links', locale=locale),
                    callback_data="menu_links")],
                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='main-menu-stadburo', locale=locale),
                    callback_data="menu_stadburo")],
                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='main-menu-settings', locale=locale),
                    callback_data="menu_settings")],
                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='main-menu-donation', locale=locale),
                    callback_data="menu_donations")],
                [InlineKeyboardButton(
                    text=await self.translation_service.translate(message_id='menu-feedback-button', locale=locale),
                    callback_data="menu_feedback")],

                # [InlineKeyboardButton(text=l10n.format_value('main-menu-additionally'), callback_data="menu_additionally")],
            ]
        )
        return main_menu
