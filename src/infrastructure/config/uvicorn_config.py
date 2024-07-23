import logging
from datetime import datetime

from fastapi import FastAPI
import uvicorn
import os
from contextlib import asynccontextmanager
from infrastructure.config import webhook_config, dispatcher_config
from infrastructure.config.bot_config import bot
import time

from infrastructure.web.api import router

system_logger = logging.getLogger("system_logger")


@asynccontextmanager
async def lifespan(app):
    # await bot.set_my_commands(get_bot_commands())

    dispatcher_config.config()
    # config_scheduler.config()

    system_logger.info("Start webhook configuration")

    time_start_webhook_config = datetime.now()
    await webhook_config.config(bot=bot)
    system_logger.info(f"Время запуска бота: {datetime.now() - time_start_webhook_config}")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)


def config():
    system_logger.info("Start uvicorn configuration")
    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("WEBAPP_PORT", 8000)))
