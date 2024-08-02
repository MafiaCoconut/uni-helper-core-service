import os
import requests
from aiogram.types import CallbackQuery

from application.interfaces.telegram_interface import TelegramInterface
from infrastructure.config.logs_config import log_decorator
from infrastructure.config.bot_config import bot


class TelegramInterfaceImpl(TelegramInterface):
    @staticmethod
    @log_decorator
    async def send_message(user_id: int, message: str, keyboard=None, parse_mode: str = "HTML"):
        await bot.send_message(chat_id=user_id, text=message, parse_mode=parse_mode, reply_markup=keyboard)

    @staticmethod
    @log_decorator
    async def send_message_to_admin(message: str, keyboard=None, parse_mode: str = "HTML"):
        await bot.send_message(chat_id=603789543, text=message, parse_mode=parse_mode, reply_markup=keyboard)

    @staticmethod
    @log_decorator
    async def edit_message_with_callback(callback: CallbackQuery, message: str, keyboard: None):
        await callback.message.edit_text(text=message, reply_markup=keyboard)
