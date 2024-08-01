import os
import requests
from application.interfaces.telegram_interface import TelegramInterface
from infrastructure.config.logs_config import log_decorator
from infrastructure.config.bot_config import bot

class TelegramInterfaceImpl(TelegramInterface):
    @staticmethod
    @log_decorator
    async def send_message(user_id: int, message: str, keyboard=None, parse_mode: str = "HTML"):
        await bot.send_message(chat_id=user_id, text=message, parse_mode=parse_mode, reply_markup=keyboard)
        # url = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage"
        # payload = {
        #     'chat_id': user_id,
        #     'text': message,
        #     'parse_mode': parse_mode
        # }
        # response = requests.post(url, data=payload)
        # print(response.json())
        # return response.json()/

    @staticmethod
    @log_decorator
    async def send_message_to_admin(message: str, keyboard=None, parse_mode: str = "HTML"):
        await bot.send_message(chat_id=603789543, text=message, parse_mode=parse_mode, reply_markup=keyboard)

        # url = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage"
        # payload = {
        #     'chat_id': 603789543,
        #     'text': message,
        #     'parse_mode': parse_mode,
        #     'reply_markup': keyboard
        # }
        # response = requests.post(url, data=payload)
        # print(response.json())
        # return response.json()
