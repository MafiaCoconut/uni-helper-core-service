import os
import requests
from aiogram.types import CallbackQuery

from application.interfaces.telegram_interface import TelegramInterface
from infrastructure.config.logs_config import log_decorator
from infrastructure.config.bot_config import bot


class TelegramInterfaceImpl(TelegramInterface):
    @staticmethod
    @log_decorator
    async def send_message(user_id: int, message: str, keyboard=None, parse_mode: str = "HTML")-> int:
        message = await bot.send_message(chat_id=user_id, text=message, parse_mode=parse_mode, reply_markup=keyboard)
        return message.message_id

    @staticmethod
    @log_decorator
    async def send_message_to_admin(message: str, keyboard=None, parse_mode: str = "HTML") -> int:
        message = await bot.send_message(chat_id=603789543, text=message, parse_mode=parse_mode, reply_markup=keyboard)
        return message.message_id

    @staticmethod
    @log_decorator
    async def edit_message_with_callback(callback: CallbackQuery, message: str, keyboard=None) -> int:
        message = await callback.message.edit_text(text=message, reply_markup=keyboard)
        return message.message_id

    @staticmethod
    @log_decorator
    async def delete_message(chat_id: int, message_id: int):
        await bot.delete_message(chat_id=chat_id, message_id=message_id)

    @staticmethod
    @log_decorator
    async def delete_keyboard(chat_id: int, message_id: int):
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)


