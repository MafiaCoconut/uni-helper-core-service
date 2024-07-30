from aiogram import Router, types, F
from aiogram.types import Message

# from utils.logs import send_log
# from handlers import auxiliary
# from keyboards import inline
from fluent.runtime import FluentLocalization

from application.services.translation_service import TranslationService
import requests


tag = "bot_messages"


class MissMessageHandler:
    def __init__(self, translation_service: TranslationService):
        self.translation_service = translation_service

    def get_router(self) -> Router:
        router = Router()
        self.__register_handlers(router)
        return router

    def __register_handlers(self, router):
        router.message()(self.echo_text_handler)

    async def echo_text_handler(self, message: Message, locale: str = 'ru') -> None:
        """Функция вывода заглушки на необъявленное сообщение/команду"""

        await message.answer(await self.translation_service.translate('echo', locale=locale))


        # url = "https://api.telegram.org/bottoken/sendMessage"
        #
        # payload = {
        #     "text": "Повторите попытку",
        #     "parse_mode": "Optional",
        #     "disable_web_page_preview": False,
        #     "disable_notification": False,
        #     "reply_to_message_id": None
        # }
        # headers = {
        #     "accept": "application/json",
        #     "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
        #     "content-type": "application/json"
        # }
        #
        # response = requests.post(url, json=payload, headers=headers)
        #
        # print(response.text)
        # await message.answer("Повторите попытку")


    # @router.message(F.document)
    # async def handle_docs(message: types.Message):
    #     # Путь, куда будет сохранён файл
    #     destination = "data/" + 'users_data'
    #
    #     # Скачивание файла
    #     await message.document.download(destination=destination)
    #
    #     # Отправка подтверждения пользователю
    #     await message.answer(f"Файл {message.document.file_name} сохранён!")

"""
https://api.telegram.org/bot6353754189:AAGWMFJEgWLeLI0f1QTyenf8jUk1ITQEVss/sendMessage?chat_id=603789543,text="Повторите попытку"

"""



