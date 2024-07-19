from aiogram import Bot, types
import os

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))


def get_bot_commands():
    """
    Функция передаёт телеграмму список команд для быстрого доступа из меню

    :return: None
    """

    bot_commands = [
        types.BotCommand(command="/main_menu", description="Открыть главное меню"),
        # types.BotCommand(command="/add_chat_to_company", description="Добавить групповой чат в компанию"),
        # types.BotCommand(command="/registration", description="Регистрация в боте"),
    ]
    return bot_commands
