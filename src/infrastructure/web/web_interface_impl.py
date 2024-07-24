import logging

from icecream import ic

from application.interfaces.web_interface import WebInterface
import aiohttp

import os
from dotenv import load_dotenv

from domain.entities.user import User

load_dotenv()

error_logger = logging.getLogger('error_logger')


class WebInterfaceImpl(WebInterface):
    async def get_canteens_menu(self, canteen_id: int):
        """
        Функция обращается к hessen-mensen-parser и возвращает текст меню определённой столовой в формате json

        :param canteen_id: Номер столовой в бд
        :param locale: Код язык на котором нужно получить меню
        :return: dict{'menu': str, 'error': {'type': str, 'text': str}}
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('CANTEEN_ADDRESS')}/canteens_menu/{canteen_id}",
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    async def get_canteens_info(self, canteen_id: int):
        print("get_canteens_info")
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('CANTEEN_ADDRESS')}/canteens/{canteen_id}",
            ) as resp:
                print(resp)

    async def parse_canteen(self,  canteen_id: int | str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('CANTEEN_ADDRESS')}/parser/{canteen_id}"
            ) as resp:
                print(resp)

    async def parse_canteen_all(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('CANTEEN_ADDRESS')}/parser/all"
            ) as resp:
                print(resp)

    async def get_termins_text(self, category_of_termins_id: str, locale: str):
        """
        Функция обращается к hessen-mensen-parser и возвращает текст меню определённой столовой в формате json

        :param category_of_termins_id: Номер категории stadburo в бд
        :param locale: Код язык на котором нужно получить текст
        :return: dict{'text': str, 'error': None}
        """
        print("get_termins_text")
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('STADBURO_ADDRESS')}/category_of_termins/{category_of_termins_id}",
                    params={'locale': locale}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    "/category_of_termins/{category_of_termins}"

    async def parse_stadburo(self, category_of_termins_id: int | str):
        print("parse_stadburo")
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('STADBURO_ADDRESS')}/parser/{category_of_termins_id}",
                    params={'get_result': True}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    async def parse_stadburo_all(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('STADBURO_ADDRESS')}/parser/all"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    async def create_user(self, user: User):
        async with aiohttp.ClientSession as session:
            async with session.post(
                f"{os.getenv('USERS_ADDRESS')}/users",
                params={'user': user}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    async def update_user_data(self, user_id: int,
                               new_mailing_time:str = None,
                               new_language: str = None,
                               new_canteen_id: int = None,
                               status: str = None,
                               ):
        async with aiohttp.ClientSession() as session:
            async with session.put(
                f"{os.getenv('USERS_ADDRESS')}/users/{user_id}",
                params={
                    'new_mailing_time': new_mailing_time,
                    'new_language': new_language,
                    'new_canteen_id': new_canteen_id,
                }
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    async def deactivate_user(self, user_id):
        async with aiohttp.ClientSession() as session:
            async with session.put(
                f"{os.getenv('USERS_ADDRESS')}/users/deactivate/{user_id}"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    async def reactivate_user(self, user_id):
        async with aiohttp.ClientSession() as session:
            async with session.put(
                f"{os.getenv('USERS_ADDRESS')}/users/reactivate/{user_id}"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    async def get_users_all(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{os.getenv('USERS_ADDRESS')}/users/all"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    async def get_user(self, user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{os.getenv('USERS_ADDRESS')}/users/{user_id}"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    async def get_users_mailing_time(self, user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{os.getenv('USERS_ADDRESS')}/users/mailing_time/{user_id}"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    async def get_users_language(self, user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{os.getenv('USERS_ADDRESS')}/users/language/{user_id}"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    async def get_users_canteen_id(self, user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{os.getenv('USERS_ADDRESS')}/users/canteen_id/{user_id}"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")




"""

async with aiohttp.ClientSession() as session:

async with session.post(FIRST_SERVICE_URL, json={"username_status": result, 'username': username}) as resp:

"""

