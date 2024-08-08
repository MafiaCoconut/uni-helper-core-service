import aiohttp
from datetime import datetime
import os
import logging
from icecream import ic

from application.gateways.users_gateway import UsersGateway
from domain.entities.user import User
from infrastructure.config.logs_config import log_decorator

error_logger = logging.getLogger('error_logger')


class UsersGatewayImpl(UsersGateway):
    users_address = os.getenv('USERS_ADDRESS')
    
    @log_decorator
    async def create_user(self, user: User):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url=self.users_address + "/users/createUser",
                    json={'user': user.model_dump()}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def update_user_data(
            self, user_id: int,
            new_status: str = None, new_mailing_time: str = None, new_locale: str = None, new_canteen_id: int = None,
    ):
        async with aiohttp.ClientSession() as session:
            async with session.put(
                    url=self.users_address + f"/user{user_id}/updateData",
                    json={
                        'new_mailing_time': new_mailing_time,
                        'new_locale': new_locale,
                        'new_canteen_id': new_canteen_id,
                    },
                    headers={'Content-Type': 'application/json'}
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
                    url=self.users_address + f"/user{user_id}/deactivate"
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
                url=self.users_address + f"/user{user_id}/reactivate"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def get_users_all(self) -> list[User]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.users_address + "/users/getAll"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def get_user(self, user_id: int) -> User:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.users_address + f"/user{user_id}/getData"
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
    async def get_users_mailing_time(self, user_id: int) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.users_address + f"/user{user_id}/getMailingTime"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def get_users_locale(self, user_id: int) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.users_address + f"/user{user_id}/getLanguage"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @log_decorator
    async def get_users_canteen_id(self, user_id: int) -> int:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=self.users_address + f"/user{user_id}/getCanteenId"
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
                    url=self.users_address + f"/user{user_id}/checkExistence"
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    ic(response_json)
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")
