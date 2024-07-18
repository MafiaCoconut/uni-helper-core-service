from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from icecream import ic

# from models.postgres.users import get_info_from_user
# from utils.fluent_main import list_of_l10n


class CheckLanguageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        # print("Before handler")
        try:
            pass
            # user_id = data["event_from_user"].id
            # language = get_info_from_user(user_id, 'language')[0]
            # ic(language)
            # l10n = list_of_l10n[language]
            # data['language'] = 'en'
            # data['l10n'] = l10n

        except Exception as e:
            pass
            # data['language'] = 'en'
            # data['l10n'] = list_of_l10n['en']

        result = await handler(event, data)

        # print("After handler")
        return result
