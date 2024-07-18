from aiogram import Dispatcher

from application.telegram.middlewares.languages import CheckLanguageMiddleware
from application.telegram.middlewares.set_logs import SetLogMiddleware


def config(dp: Dispatcher):
    pass
    # dp.message.middleware(CheckLanguageMiddleware())
    # dp.callback_query.middleware(SetLogMiddleware())
