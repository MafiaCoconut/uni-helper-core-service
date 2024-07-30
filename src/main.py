# import asyncio
# import logging
#
# from aiogram import Bot, Dispatcher
# import os
# from aiohttp import web
# from aiogram.types import Update
# from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
# from infrastructure.config.bot_config import bot, get_bot_commands
import logging

# from infrastructure.repositories_impl.postgres.postgres_connection import close_all_connections
# from infrastructure.config.scheduler import config_scheduler
from infrastructure.config import webhook_config, logs_config, uvicorn_config


# @uvicorn_config.app.post("/webhook")
# async def bot_webhook(update: dict):
#     telegram_update = Update(**update)
#     print(telegram_update)
#     await dispatcher_config.dp._process_update(bot=bot, update=telegram_update, call_answer=True)


def start_bot():
    try:
        uvicorn_config.config()
    except Exception as e:
        print(e)
        logging.warning(e)
    finally:
        pass
        # close_all_connections()


if __name__ == "__main__":
    # logs_config.config()

    start_bot()

