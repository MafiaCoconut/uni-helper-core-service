import os
import requests
from application.interfaces.telegram_interface import TelegramInterface


class TelegramInterfaceImpl(TelegramInterface):
    @staticmethod
    async def send_message(user_id: int, message: str, keyboard: None):
        url = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage"
        payload = {
            'chat_id': user_id,
            'text': message
        }
        response = requests.post(url, data=payload)
        return response.json()


