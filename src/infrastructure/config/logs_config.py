import logging
from dotenv import load_dotenv
import os


load_dotenv()
system_logger = logging.getLogger("system_logger")
user_logger = logging.getLogger("user_logger")
error_logger = logging.getLogger("error_logger")


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

    global system_logger
    global user_logger

    if os.getenv("DEVICE") == "Laptop" or os.getenv("DEVICE") == "Ubuntu":
        # logging.basicConfig(
        #     format="[%(levelname)s] %(asctime)s - %(message)s",
        #     datefmt="%d.%m-%H:%M",
        #     handlers=[
        #         logging.StreamHandler()  # Вывод логов в консоль
        #     ]
        # )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        system_logger.setLevel(logging.DEBUG)
        user_logger.setLevel(logging.DEBUG)

        system_logger.addHandler(console_handler)
        user_logger.addHandler(console_handler)


    else:
        system_logger.setLevel(logging.INFO)
        user_logger.setLevel(logging.DEBUG)

        # global error_logger
        # error_logger.setLevel(logging.ERROR)
        # error_logger.addHandler(error_handler)

        # from infrastructure.telegram.utils.registration_dispatcher import dp
        # dp.errors.register(error_aio_handler)

    system_logger.addHandler(system_handler)

    apscheduler_logger = logging.getLogger("apscheduler")
    apscheduler_logger.setLevel(logging.DEBUG)
    apscheduler_logger.addHandler(system_handler)

    aiogram_logger = logging.getLogger("aiogram")
    aiogram_logger.setLevel(logging.DEBUG)
    aiogram_logger.addHandler(system_handler)

    user_logger.setLevel(logging.DEBUG)
    user_logger.addHandler(user_handler)



    # raise RuntimeError("Test unhandled")