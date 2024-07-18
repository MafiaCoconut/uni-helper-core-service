from aiogram import Dispatcher
# from application.telegram.handlers.miss_message_handlers import router as message_handlers_router
from infrastructure.config.handlers_config import miss_message_handler

def include_routers(dp: Dispatcher):
    dp.include_router(miss_message_handler.get_router())
