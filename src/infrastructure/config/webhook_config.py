import logging
import requests

import ngrok
import os

from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web

from aiogram import Dispatcher, Bot

system_logger = logging.getLogger('system_logger')


async def config(bot: Bot, dp: Dispatcher):
    system_logger.info("Start webhook configuration")

    requests.post(f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/setWebhook?url={os.getenv('NGROK_LINK')}/webhook")

    system_logger.info("После установки webhook")

