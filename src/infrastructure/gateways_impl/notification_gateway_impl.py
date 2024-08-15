import aiohttp
from datetime import datetime
import os
import logging
from icecream import ic

from application.gateways.notification_gateway import NotificationGateway
from infrastructure.config.logs_config import log_decorator


class NotificationGatewayImpl(NotificationGateway):
    notification_address = os.getenv('NOTIFICATION_ADDRESS')

    @log_decorator
    async def update_mailing_time(self, user_id: int, new_mailing_time: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.notification_address + f"/user{user_id}/updateMailingTime",
                    json={'new_mailing_time': new_mailing_time}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                else:
                    logging.error(f"Failed to update mailing time. Response code: {resp.status}")

    @log_decorator
    async def delete_mailing_time(self, user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.notification_address + f"/user{user_id}/deleteMailingTime",
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                else:
                    logging.error(f"Failed to update mailing time. Response code: {resp.status}")

    @log_decorator
    async def set_mailing_time(self, user_id: int, mailing_time: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.notification_address + f"/user{user_id}/addUsersMailingTime",
                    json={'mailing_time': mailing_time}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                else:
                    logging.error(f"Failed to update mailing time. Response code: {resp.status}")
