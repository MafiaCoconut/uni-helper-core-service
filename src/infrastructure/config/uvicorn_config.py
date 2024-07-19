from fastapi import FastAPI
import uvicorn
import os
from contextlib import asynccontextmanager
from infrastructure.config import webhook_config, dispatcher_config
from infrastructure.config.bot_config import bot


@asynccontextmanager
async def lifespan(app):
    # await bot.set_my_commands(get_bot_commands())

    # Set routers and callbacks in
    dispatcher_config.config()
    # config_scheduler.config()
    print('fdsggfbdsfdvf')
    await webhook_config.config(bot=bot)
    yield

app = FastAPI(lifespan=lifespan)


def config():
    # uvicorn_config = uvicorn.Config(app, host="localhost", port=8080, log_level="debug")
    # server = uvicorn.Server(uvicorn_config)
    # server.run()
    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("WEBAPP_PORT", 8000)))
