from aiogram import Dispatcher

from application.telegram.middlewares.languages import CheckLanguageMiddleware
from application.telegram.middlewares.set_logs import SetLogMiddleware


def config(dp: Dispatcher):

    # dp.message.middleware(CheckLanguageMiddleware())
    dp.message.middleware(SetLogMiddleware())
    dp.callback_query.middleware(SetLogMiddleware())
