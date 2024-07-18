import logging
from dotenv import load_dotenv
import os

load_dotenv()
system_logger = logging.getLogger('system_logging')
user_logger = logging.getLogger('user_logging')
mensa_logger = logging.getLogger('mensa')


def set_func(function: str, tag: str, status: str = "info"):
    result = f"Called Tag:[{tag}] Function:({function})"
    if status == "info":
        system_logger.info(result)
    elif status == "debug":
        system_logger.debug(result)


def set_inside_func(function, tag, data, status="info"):
    result = f"[{tag}] [{function}]: {data}"
    if status == "info":
        system_logger.info(result)
    elif status == "debug":
        system_logger.debug(result)
    elif status == 'error':
        system_logger.error(result)


def set_func_and_person(function, tag, message, status="info"):
    result = f"User: {message.chat.username}/{message.chat.id} Tag: [{tag}]  Function: ({function})"
    if status == "info":
        user_logger.info(result)
        system_logger.info(result)
    elif status == "debug":
        user_logger.debug(result)
        system_logger.debug(result)


def send_log(message):
    result = f'User: {message.chat.username}/{message.chat.id} Send Message: "{message.text}"'
    user_logger.info(result)
    system_logger.debug(result)


def add_or_delete_user(message, command):
    if command == "add":
        result = f'Add User: {message.chat.username}/{message.chat.id}'
    else:
        result = f'Delete User: {message.chat.username}/{message.chat.id}'

    user_logger.info(result)
    system_logger.info(result)


def config():
    # Максимально подробный вывод логов
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')

    # Нормальный вывод логов
    formatter = logging.Formatter(fmt='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d.%m-%H:%M')

    # Настройка вывода данных в файлы
    system_handler = logging.FileHandler('logs/system_data.log')
    system_handler.setFormatter(formatter)

    # mensa_handler = logging.FileHandler('data/logs/mensa_data.log')
    # mensa_handler.setFormatter(formatter)

    user_handler = logging.FileHandler('logs/user_data.log')
    user_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    global system_logger
    if os.getenv("DEVICE") in ["Laptop", "Ubuntu", "RaspberryTest"]:
        system_logger.setLevel(logging.DEBUG)
    else:
        system_logger.setLevel(logging.INFO)
    system_logger.addHandler(system_handler)
    system_logger.addHandler(console_handler)

    apscheduler_logger = logging.getLogger('apscheduler')
    apscheduler_logger.setLevel(logging.DEBUG)
    apscheduler_logger.addHandler(system_handler)
    apscheduler_logger.addHandler(console_handler)

    # aiogram_logger = logging.getLogger('aiogram')
    # aiogram_logger.setLevel(logging.DEBUG)
    # aiogram_logger.addHandler(system_handler)

    # global mensa_logger
    # mensa_logger.setLevel(logging.DEBUG)
    # mensa_logger.addHandler(mensa_handler)

    global user_logger
    user_logger.setLevel(logging.DEBUG)
    user_logger.addHandler(user_handler)
    user_logger.addHandler(console_handler)

    # # Настройка логгера Uvicorn
    # uvicorn_access_logger = logging.getLogger("uvicorn.access")
    # uvicorn_access_logger.addHandler(console_handler)
    #
    # uvicorn_error_logger = logging.getLogger("uvicorn.error")
    # uvicorn_error_logger.addHandler(console_handler)