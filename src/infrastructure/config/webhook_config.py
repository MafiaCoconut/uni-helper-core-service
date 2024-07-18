import ngrok
import os
from aiohttp import web

from aiogram import Dispatcher, Bot


async def config(dp: Dispatcher, bot: Bot):
    listener = await ngrok.forward(
    int(os.getenv("WEBAPP_PORT")), authtoken=os.getenv("NGROK_AUTH_TOKEN"), 
    )
    await bot.set_webhook(f"{listener.url()}/webhook", drop_pending_updates=True)