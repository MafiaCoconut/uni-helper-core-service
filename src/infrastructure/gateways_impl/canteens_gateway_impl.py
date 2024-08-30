import aiohttp
from datetime import datetime
import os
import logging
from icecream import ic

from application.gateways.canteens_gateway import CanteensGateway
from domain.entities.canteen import Canteen
from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish
from infrastructure.config.logs_config import log_decorator

error_logger = logging.getLogger('error_logger')


class CanteensGatewayImpl(CanteensGateway):
    canteens_address = os.getenv('CANTEENS_ADDRESS')

    @log_decorator(print_args=False)
    async def get_canteens_data(self, canteen_id: int):
        """
        Функция обращается к hessen-mensen-parser и возвращает данные о столовой и её меню формате json

        :param canteen_id: Номер столовой в бд
        :return: dict{'canteen': Canteen, 'main_dishes': list[MainDish], 'side_dishes': list[SideDish]}
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.canteens_address + f"/canteen{canteen_id}/getDishes",
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    # ic(response_json)
                    canteen = Canteen(
                        canteen_id=response_json.get('canteen').get('canteen_id'),
                        name=response_json.get('canteen').get('name'),
                        description=response_json.get('canteen').get('description'),
                        status=response_json.get('canteen').get('status'),
                        times=response_json.get('canteen').get('times'),
                        last_parsing_time=response_json.get('canteen').get('last_parsing_time'),
                        opened_time=response_json.get('canteen').get('opened_time'),
                        closed_time=response_json.get('canteen').get('closed_time'),
                        created_at=datetime.fromisoformat(response_json.get('canteen').get('created_at')),
                    )
                    # ic(canteen)
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
                            side_dish_id=side_dish.get('side_dish_id'),
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

    @log_decorator(print_args=False)
    async def get_canteens_info(self, canteen_id: int) -> Canteen:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.canteens_address + f"/canteen{canteen_id}/getObject",
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    # ic(response_json)
                    canteen = Canteen(
                        canteen_id=response_json.get('canteen').get('canteen_id'),
                        name=response_json.get('canteen').get('name'),
                        description=response_json.get('canteen').get('description'),
                        status=response_json.get('canteen').get('status'),
                        times=response_json.get('canteen').get('times'),
                        last_parsing_time=response_json.get('canteen').get('last_parsing_time'),
                        opened_time=response_json.get('canteen').get('opened_time'),
                        closed_time=response_json.get('canteen').get('closed_time'),
                        created_at=datetime.fromisoformat(response_json.get('canteen').get('created_at')),
                    )
                    # ic(canteen)
                    return canteen
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator(print_args=False)
    async def parse_canteen(self, canteen_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url=self.canteens_address + f"/canteen{canteen_id}/startParser"
            ) as resp:
                print(resp)

    @log_decorator(print_args=False)
    async def parse_canteen_all(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url=self.canteens_address + "/canteen/startAllParsers"
            ) as resp:
                print(resp)

    @log_decorator(print_args=False)
    async def reactivate(self, canteen_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.put(
                    url=self.canteens_address + f"/canteen{canteen_id}/reactivate"
            ) as resp:
                print(resp)

    @log_decorator(print_args=False)
    async def deactivate(self, canteen_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.put(
                    url=self.canteens_address + f"/canteen{canteen_id}/deactivate"
            ) as resp:
                print(resp)

