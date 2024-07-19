import ngrok
import os
from aiohttp import web

from aiogram import Dispatcher, Bot


async def config(bot: Bot):
    print("начала конфигурации webhook")
    listener = await ngrok.forward(
    int(os.getenv("WEBAPP_PORT")), authtoken=os.getenv("NGROK_AUTH_TOKEN"), 
    )
    print(listener.url())
    print(listener)
    await bot.set_webhook(f"{listener.url()}/webhook", drop_pending_updates=True)