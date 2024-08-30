import aiohttp
from datetime import datetime
import os
import logging
from icecream import ic

from application.gateways.stadburo_gateway import StadburoGateway
from domain.entities.category_of_termin import CategoryOfTermins
from domain.entities.termin import Termin
from infrastructure.config.logs_config import log_decorator

error_logger = logging.getLogger('error_logger')


class StadburoGatewayImpl(StadburoGateway):
    stadburo_address = os.getenv('STADBURO_ADDRESS')

    @log_decorator(print_args=False)
    async def parse_stadburo(self, category_of_termins_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.stadburo_address + f"/category_of_termins{category_of_termins_id}/startParser",
                    params={'get_result': True}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    # ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator(print_args=False)
    async def parse_stadburo_all(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url=self.stadburo_address + f"/category_of_termins/startParsersAll"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    # ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator(print_args=False)
    async def get_category_of_termins_data(self, category_of_termins_id: int):
        """
        Функция обращается к marburg-stadburo-parser и возвращает данные о категории и терминах

        :param category_of_termins_id: Номер категории stadburo в бд
        :return: dict{'termins': list[Termin], 'category_of_termins': CategoryOfTermins, 'error': None}
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.stadburo_address + f"/category_of_termins{category_of_termins_id}/getData"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    # ic(response_json)
                    result = {}
                    result['error'] = response_json.get('error')
                    # ic(response_json.get('termins')[0].get('created_at'))
                    # ic(type(response_json.get('termins')[0].get('created_at')))
                    result['termins'] = [Termin(
                        termin_id=termin.get('termin_id'),
                        category_id=termin.get('category_id'),
                        time=datetime.fromisoformat(termin.get('time')),
                        created_at=datetime.fromisoformat(termin.get('created_at'))
                    ) for termin in response_json.get('termins')]

                    result['category_of_termins'] = CategoryOfTermins(
                        category_id=response_json.get('category_of_termins').get('category_id'),
                        name=response_json.get('category_of_termins').get('name'),
                        created_at=datetime.fromisoformat(response_json.get('category_of_termins').get('created_at')),
                    )
                    return result
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

