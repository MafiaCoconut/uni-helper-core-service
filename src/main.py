import asyncio
import logging

from aiogram import Bot, Dispatcher
import os
# from aiohttp import web
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from infrastructure.logging.logs_setup import logs_settings
from infrastructure.config.bot_config import bot, get_bot_commands
from infrastructure.config import dispatcher_config
from infrastructure.config import uvicorn_config
# from infrastructure.repositories_impl.postgres.postgres_connection import close_all_connections
# from infrastructure.config.scheduler import config_scheduler
from infrastructure.config import webhook_config



@uvicorn_config.app.post(f"/webhook")
async def bot_webhook(update: dict):
    telegram_update = Update(**update)
    await dispatcher_config.dp._process_update(bot=bot, update=telegram_update, call_answer=True)



# @uvicorn_config.app.on_event("startup")
# async def on_startup(dispatcher: Dispatcher = None):
#     await bot.set_my_commands(get_bot_commands())
#
#     # Set routers and callbacks in
#     dispatcher_config.config()
#     # config_scheduler.config()
#     print('fdsggfbdsfdvf')
#     print("начала конфигурации webhook")
#     await webhook_config.config(bot=bot)




def start_bot():
    # bot.set_webhook(os.getenv('WEBHOOK_URL'))
    # app = web.Application()
    # webhook_requests_handler = SimpleRequestHandler(
    #     dispatcher=dispatcher_config.dp,
    #     bot=bot,
    #     secret_token=os.getenv("WEBHOOK_TOKEN"),
    #
    # )
    # webhook_requests_handler.register(app, path="/webhook")
    # asyncio.run(on_startup())

    try:
        # dispatcher_config.dp.startup.register(on_startup)
        # setup_application(app, dispatcher_config.dp, bot=bot)
        print("Запуск бота")
        # asyncio.run(on_startup())
        # import uvicorn

        uvicorn_config.config()

        # web.run_app(
        # app,
        # host=os.getenv("WEBAPP_HOST"),
        # port=int(os.getenv("WEBAPP_PORT"))
        # )
    except Exception as e:
        print(e)
        logging.warning(e)
    finally:
        pass
        # close_all_connections()



if __name__ == "__main__":
    # logs_settings()

    start_bot()
