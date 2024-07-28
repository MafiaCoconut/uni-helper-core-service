import logging
from typing import Dict, List, Any

from icecream import ic
from datetime import datetime
from application.interfaces.web_interface import WebInterface
import aiohttp

import os
from dotenv import load_dotenv

from domain.entities.canteen import Canteen
from domain.entities.category_of_termin import CategoryOfTermins
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish
from domain.entities.termin import Termin
from domain.entities.user import User
from infrastructure.config.logs_config import log_decorator

load_dotenv()

error_logger = logging.getLogger('error_logger')


class WebInterfaceImpl(WebInterface):
    @log_decorator
    async def get_canteens_data(self, canteen_id: int) -> dict[Canteen | list[MainDish] | list[SideDish]]:
        """
        Функция обращается к hessen-mensen-parser и возвращает текст меню определённой столовой в формате json

        :param canteen_id: Номер столовой в бд
        :return: dict{'canteen': Canteen, 'main_dishes': list[MainDish], 'side_dishes': list[SideDish]}
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('CANTEEN_ADDRESS')}/canteens_menu/{canteen_id}",
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    canteen = Canteen(
                        canteen_id=response_json.get('canteen').get('canteen_id'),
                        name=response_json.get('canteen').get('name'),
                        description=response_json.get('canteen').get('description'),
                        opened_time=response_json.get('canteen').get('opened_time'),
                        closed_time=response_json.get('canteen').get('closed_time'),
                        created_at=datetime.fromisoformat(response_json.get('canteen').get('created_at')),
                    )
                    main_dishes = []
                    side_dishes = []
                    if response_json.get('main_dishes') is not None:
                        main_dishes = [MainDish(
                            main_dish_id=main_dish.get('main_dish_id'),
                            canteen_id=main_dish.get('canteen_id'),
                            name=main_dish.get('name'),
                            type=main_dish.get('type'),
                            price=main_dish.get('price'),
                            properties=main_dish.get('properties'),
                            created_at=datetime.fromisoformat(main_dish.get('created_at')),
                            updated_at=datetime.fromisoformat(main_dish.get('updated_at')),
                        ) for main_dish in response_json.get('main_dishes')]

                    if response_json.get('side_dishes') is not None:
                        side_dishes = [SideDish(
                            side_dish_id=side_dish.get('updated_at'),
                            canteen_id=side_dish.get('canteen_id'),
                            name=side_dish.get('name'),
                            type=side_dish.get('type'),
                            price=side_dish.get('price'),
                            properties=side_dish.get('properties'),
                            created_at=datetime.fromisoformat(side_dish.get('created_at')),
                            updated_at=datetime.fromisoformat(side_dish.get('updated_at')),
                        ) for side_dish in response_json.get('side_dishes')]

                    return {'canteen': canteen, 'main_dishes': main_dishes, 'side_dishes': side_dishes}
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")
                    raise ValueError(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def get_canteens_info(self, canteen_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('CANTEEN_ADDRESS')}/canteens/{canteen_id}",
            ) as resp:
                print(resp)

    @log_decorator
    async def parse_canteen(self,  canteen_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('CANTEEN_ADDRESS')}/parser/{canteen_id}"
            ) as resp:
                print(resp)

    @log_decorator
    async def parse_canteen_all(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('CANTEEN_ADDRESS')}/parser/all"
            ) as resp:
                print(resp)

    @log_decorator
    async def get_category_of_termins_data(self, category_of_termins_id: int):
        """
        Функция обращается к hessen-mensen-parser и возвращает текст меню определённой столовой в формате json

        :param category_of_termins_id: Номер категории stadburo в бд
        :param locale: Код язык на котором нужно получить текст
        :return: dict{'termins': list[Termin], 'category_of_termins': CategoryOfTermins, 'error': None}
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('STADBURO_ADDRESS')}/category_of_termins/getData",
                    params={'category_of_termins_id': category_of_termins_id}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()

                    result = {'error': response_json.get('error')}

                    result['termins'] = [Termin(
                        termin_id=termin.termin_id,
                        category_id=termin.category_id,
                        time=termin.time,
                        created_at=termin.created_at
                    ) for termin in response_json.get('termins')]

                    result['category_of_termins'] = CategoryOfTermins(
                        category_id=response_json.get('category_of_termins').category_id,
                        name=response_json.get('category_of_termins').category_id,
                        created_at=response_json.get('category_of_termins').created_at,
                    )
                    return result
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
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

    @log_decorator
    async def parse_stadburo(self, category_of_termins_id: int | str):
        print("parse_stadburo")
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('STADBURO_ADDRESS')}/parser",
                    params={'category_of_termins_id': category_of_termins_id, 'get_result': True}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
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

    @log_decorator
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

    @log_decorator
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

    @log_decorator
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

    @log_decorator
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

    @log_decorator
    async def get_user(self, user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{os.getenv('USERS_ADDRESS')}/users/{user_id}"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    user = User(
                        user_id=response_json['user_id'],
                        username=response_json['username'],
                        mailing_time=response_json['mailing_time'],
                        language=response_json['language'],
                        canteen_id=response_json['canteen_id'],
                        created_at=response_json['created_at'],
                        updated_at=response_json['updated_at'],
                        status=response_json['status'],
                    )
                    return user
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
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

    @log_decorator
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

    @log_decorator
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

