from aiogram import Router, types, F
from aiogram.types import Message

# from utils.logs import send_log
# from handlers import auxiliary
# from keyboards import inline
from fluent.runtime import FluentLocalization

from application.services.translation_service import TranslationService

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

    async def echo_text_handler(self, message: Message) -> None:
        """Функция вывода заглушки на необъявленное сообщение/команду"""

        # send_log(message)
        await message.answer(self.translation_service.translate('echo', locale='en'))
        # reply_markup=inline.get_send_menu_main(l10n))

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





