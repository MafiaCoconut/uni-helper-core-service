from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from aiogram.types import TelegramObject, Message, CallbackQuery

from infrastructure.config.handlers_config import logs_handler


class SetLogMiddleware(BaseMiddleware):
    """
    A class whose purpose is to check whether a user is registered in the database or not
    """

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        print(handler)
        print(event)
        print(data)
        if isinstance(event, Message):
            logs_handler.set_func_and_person(function=data['handler'].callback.__name__, message=event, status='debug')

        elif isinstance(event, CallbackQuery):
            logs_handler.set_func_and_person(function=data['handler'].callback.__name__, message=event.message, status='debug')

        return await handler(event, data)



