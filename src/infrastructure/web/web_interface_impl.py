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
        Функция обращается к hessen-mensen-parser и возвращает данные о столовой и её меню формате json

        :param canteen_id: Номер столовой в бд
        :return: dict{'canteen': Canteen, 'main_dishes': list[MainDish], 'side_dishes': list[SideDish]}
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('CANTEEN_ADDRESS')}/canteen{canteen_id}/getDishes",
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
                    f"{os.getenv('CANTEEN_ADDRESS')}/canteen{canteen_id}/startParser"
            ) as resp:
                print(resp)

    @log_decorator
    async def parse_canteen_all(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('CANTEEN_ADDRESS')}/canteen/startParsersAll"
            ) as resp:
                print(resp)

    @log_decorator
    async def get_category_of_termins_data(self, category_of_termins_id: int):
        """
        Функция обращается к marburg-stadburo-parser и возвращает данные о категории и терминах

        :param category_of_termins_id: Номер категории stadburo в бд
        :return: dict{'termins': list[Termin], 'category_of_termins': CategoryOfTermins, 'error': None}
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('STADBURO_ADDRESS')}/category_of_termins{category_of_termins_id}/getData"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    # ic(response_json)
                    result = {'error': response_json.get('error')}
                    ic(response_json.get('termins')[0].get('created_at'))
                    ic(type(response_json.get('termins')[0].get('created_at')))
                    result['termins'] = [Termin(
                        termin_id=termin.get('termin_id'),
                        category_id=termin.get('category_id'),
                        time=datetime.fromisoformat(termin.get('time')),
                        created_at=datetime.fromisoformat(termin.get('created_at'))
                    ) for termin in response_json.get('termins')]

                    result['category_of_termins'] = CategoryOfTermins(
                        category_id=response_json.get('category_of_termins').get('category_id'),
                        name=response_json.get('category_of_termins').get('name'),
                        # created_at=datetime.fromisoformat(response_json.get('category_of_termins').get('created_at')),
                    )
                    return result
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def parse_stadburo_all(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{os.getenv('STADBURO_ADDRESS')}/category_of_termins/startParsersAll"
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
                    f"{os.getenv('STADBURO_ADDRESS')}//category_of_termins{category_of_termins_id}/startParser",
                    params={'get_result': True}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def create_user(self, user: User):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{os.getenv('USERS_ADDRESS')}/users/createUser",
                json={'user': user.model_dump()}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def update_user_data(self, user_id: int,
                               new_mailing_time: str = None,
                               new_locale: str = None,
                               new_canteen_id: int = None,
                               status: str = None,
                               ):
        async with aiohttp.ClientSession() as session:
            async with session.put(
                f"{os.getenv('USERS_ADDRESS')}/user{user_id}/updateData",
                params={
                    'new_mailing_time': new_mailing_time,
                    'new_locale': new_locale,
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
                f"{os.getenv('USERS_ADDRESS')}/user{user_id}/deactivate"
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
                f"{os.getenv('USERS_ADDRESS')}/user{user_id}/reactivate"
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
                f"{os.getenv('USERS_ADDRESS')}/users/getAll"
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
                f"{os.getenv('USERS_ADDRESS')}/user{user_id}/getData"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    if response_json is not None:
                        user = User(
                            user_id=response_json.get('user_id'),
                            username=response_json.get('username'),
                            name=response_json.get('name'),
                            mailing_time=response_json.get('mailing_time'),
                            locale=response_json.get('locale'),
                            canteen_id=response_json.get('canteen_id'),
                            created_at=datetime.fromisoformat(response_json.get('created_at')),
                            updated_at=datetime.fromisoformat(response_json.get('updated_at')),
                            status=response_json.get('status'),
                        )
                        return user
                    else:
                        raise ValueError('The user is missing')
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def get_users_mailing_time(self, user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{os.getenv('USERS_ADDRESS')}/user{user_id}/getMailingTime"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def get_users_locale(self, user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{os.getenv('USERS_ADDRESS')}/user{user_id}/getLanguage"
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
                f"{os.getenv('USERS_ADDRESS')}/user{user_id}/getCanteenId"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def user_check_existence(self, user_id: int) -> bool:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{os.getenv('USERS_ADDRESS')}/user{user_id}/checkExistence"
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

