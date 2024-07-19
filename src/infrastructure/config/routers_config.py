from aiogram import Dispatcher
# from application.telegram.handlers.miss_message_handlers import router as message_handlers_router
from infrastructure.config.handlers_config import (miss_message_handler, user_commands_handler, menu_main_handler,
                                                   canteens_handler, donations_handler, stadburo_handler, links_handler)


def include_routers(dp: Dispatcher):
    dp.include_router(menu_main_handler.get_router())
    dp.include_router(canteens_handler.get_router())
    dp.include_router(stadburo_handler.get_router())
    dp.include_router(donations_handler.get_router())
    dp.include_router(links_handler.get_router())

    dp.include_router(user_commands_handler.get_router())
    dp.include_router(miss_message_handler.get_router())

