import logging
from typing import Callable, Dict, Any, Awaitable

import redis
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from icecream import ic

from application.services.users_service import UsersService


# from models.postgres.users import get_info_from_user
# from utils.fluent_main import list_of_l10n
error_logger = logging.getLogger('error_logger')

class CheckLocaleMiddleware(BaseMiddleware):
    def __init__(self, redis_client: redis.Redis, users_service: UsersService):
        self.users_service = users_service
        self.redis_client = redis_client

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        try:
            # print("Before handler")
            user_id = data["event_from_user"].id
            locale_key = f"{user_id}:locale"
            locale = self.redis_client.get(locale_key)
            ic(f"From redis: {locale}")
            if not locale:
                try:
                    locale = await self.users_service.get_users_locale(user_id=user_id)
                    ic(f"From DB: {locale}")
                except ValueError:
                    error_logger.error("Пользователь отсутствует")
                    locale = "en"
                if locale:
                    self.redis_client.setex(name=locale_key, time=3600, value=locale)
                else:
                    locale = "en"

            data['locale'] = locale


            # user_id = data["event_from_user"].id
            # language = get_info_from_user(user_id, 'language')[0]
            # ic(language)
            # l10n = list_of_l10n[language]
            # data['language'] = 'en'
            # data['l10n'] = l10n

        except Exception as e:
            error_logger.error(e)
            # data['language'] = 'en'
            # data['l10n'] = list_of_l10n['en']

        result = await handler(event, data)

        # print("After handler")
        return result
