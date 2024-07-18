from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
import os


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return str(message.chat.id) in os.getenv("ADMINS_ID").split(',')


class IsAdminCallback(BaseFilter):
    async def __call__(self, call: CallbackQuery) -> bool:
        return str(call.message.chat.id) in os.getenv("ADMINS_ID").split(',')

