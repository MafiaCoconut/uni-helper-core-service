import logging
from datetime import datetime
from aiogram.types import Update
from fastapi import FastAPI, Request
import uvicorn
import os
from contextlib import asynccontextmanager

from icecream import ic

from infrastructure.config import webhook_config, dispatcher_config, logs_config
from infrastructure.config.bot_config import bot
import time

from infrastructure.config.services_config import get_scheduler_service


from infrastructure.config.dispatcher_config import dp
from infrastructure.web.api import router

system_logger = logging.getLogger("system_logger")
error_logger = logging.getLogger("error_logger")


@asynccontextmanager
async def lifespan(app):
    logs_config.config()

    scheduler_service = get_scheduler_service()
    await scheduler_service.set_start_jobs()
    system_logger.info("Start uvicorn configuration")

    # await bot.set_my_commands(get_bot_commands())

    dispatcher_config.config()
    # config_scheduler.config()

    time_start_webhook_config = datetime.now()
    await webhook_config.config(bot=bot, dp=dp)
    system_logger.info(f"Время запуска бота: {datetime.now() - time_start_webhook_config}")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)


def config():
    system_logger.info("Start uvicorn configuration")
    uvicorn.run(app, host=os.getenv("WEBAPP_HOST", "127.0.0.1"), port=int(os.getenv("WEBAPP_PORT", 8000)))


@app.post("/webhook")
async def bot_webhook(request: Request):
    data = await request.json()
    update = Update(**data)
    # ic(update)
    try:
        await dp.feed_update(bot=bot, update=update)
    except Exception as e:
        error_logger.error(e)
        system_logger.error(e)


@app.post("/")
async def root(request: Request):
    return {"message": "Hello World"}


if __name__ == '__main__':
    config()
