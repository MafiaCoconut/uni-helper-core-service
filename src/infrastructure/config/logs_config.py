import inspect
import logging
from functools import wraps

from dotenv import load_dotenv
import os
from aiogram.types.update import Update


load_dotenv()
system_logger = logging.getLogger("system_logger")
user_logger = logging.getLogger("user_logger")
error_logger = logging.getLogger("error_logger")
apscheduler_logger = logging.getLogger('apscheduler')
aiogram_logger = logging.getLogger("aiogram.events")


def config():
    """
    Функция первичной настройки логов

    :return: None
    """
    # Максимально подробный вывод логов
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')

    # Нормальный вывод логов
    formatter = logging.Formatter(
        fmt="[%(levelname)s] %(asctime)s - %(message)s", datefmt="%d.%m-%H:%M"
    )

    system_handler = logging.FileHandler("logs/system_data.log")
    system_handler.setFormatter(formatter)

    user_handler = logging.FileHandler("logs/user_data.log")
    user_handler.setFormatter(formatter)

    error_handler = logging.FileHandler("logs/error_data.log")
    error_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if os.getenv("MODE") == "DEVELOPMENT":
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        system_logger.setLevel(logging.DEBUG)
        user_logger.setLevel(logging.DEBUG)
        error_logger.setLevel(logging.DEBUG)

        system_logger.addHandler(console_handler)
        user_logger.addHandler(console_handler)
        error_logger.addHandler(console_handler)
        apscheduler_logger.addHandler(console_handler)

    else:
        system_logger.setLevel(logging.INFO)
        user_logger.setLevel(logging.DEBUG)
        error_logger.setLevel(logging.ERROR)

    system_logger.addHandler(system_handler)

    user_logger.addHandler(user_handler)

    error_logger.addHandler(error_handler)
    # error_logs_config(formatter=formatter)

    apscheduler_logger.setLevel(logging.DEBUG)
    apscheduler_logger.addHandler(system_handler)

    aiogram_logger.setLevel(logging.DEBUG)
    aiogram_logger.addHandler(system_handler)


async def error_aio_handler(update: Update):
    """
    Функция для обработки и логирования всех необработанных исключений.
    """
    error_logger.error(update.exception)
    system_logger.error(update.exception)


def error_logs_config(formatter):
    from infrastructure.config.dispatcher_config import dp
    dp.errors.register(error_aio_handler)


def log_decorator(log_level=logging.DEBUG, print_args=True, print_kwargs=True):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            file_path = inspect.getfile(func)
            file_name = file_path[file_path.rfind("/")+1:]
            msg = f"Called function: {file_name}[{func.__name__}]"
            if print_args:
                msg += f" Args: {args}."
            if print_kwargs:
                msg += f" Kwargs: {kwargs}"

            system_logger.log(level=log_level, msg=msg)
            result = await func(*args, **kwargs)

            return result

        return wrapper
    return decorator


# def log_handler_decorator(func, user="Some USER", log_level=logging.DEBUG):
#     @wraps(func)
#     async def wrapper(*args, **kwargs):
#         system_logger.log(level=log_level, msg=f"Called function: {func.__name__}. User: {user}")
#
#         # Выполнение функции и получение результата
#         result = await func(*args, **kwargs)
#
#         # Запись результата выполнения функции
#         # system_logger.log(level=log_level, msg=f"Result: {result}")
#
#         return result
#
#     return wrapper