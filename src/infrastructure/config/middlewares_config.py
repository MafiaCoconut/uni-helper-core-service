from aiogram import Dispatcher

from application.telegram.middlewares.check_locale_middleware import CheckLocaleMiddleware
from application.telegram.middlewares.set_logs_middleware import SetLogMiddleware
from infrastructure.config.redis_config import redis_client
from infrastructure.config.services_config import users_service


def config(dp: Dispatcher):

    # dp.message.middleware(CheckLanguageMiddleware())
    dp.message.middleware(SetLogMiddleware())
    dp.callback_query.middleware(SetLogMiddleware())

    dp.message.middleware(CheckLocaleMiddleware(redis_client=redis_client, users_service=users_service))
    dp.callback_query.middleware(CheckLocaleMiddleware(redis_client=redis_client, users_service=users_service))
