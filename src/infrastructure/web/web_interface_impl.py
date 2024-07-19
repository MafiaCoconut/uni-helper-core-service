import logging

from icecream import ic

from application.interfaces.web_interface import WebInterface
import aiohttp

CANTEENMICROSVCRPORT=8001
error_logger = logging.getLogger('error_logger')


class WebInterfaceImpl(WebInterface):
    async def get_canteens_menu(self, canteen_id: int | str, locale: str):
        print("get_canteens_menu")
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"http://127.0.0.1:8001/canteens_menu/{canteen_id}",
                    params={'locale': locale}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")




    async def get_canteens_info(self, canteen_id: int | str, locale: str):
        print("get_canteens_info")
        async with (aiohttp.ClientSession() as session):
            async with session.get(
                    f"http://localhost:8001/canteens/{canteen_id}",
                    json={'locale': locale}
            ) as resp:
                print(resp)

    async def parse_canteen(self,  canteen_id: int | str):
        async with (aiohttp.ClientSession() as session):
            async with session.get(
                    f"localhost/parser/{canteen_id}"
            ) as resp:
                print(resp)

    async def parse_canteen_all(self):
        async with (aiohttp.ClientSession() as session):
            async with session.get(
                    f"localhost/parser/all"
            ) as resp:
                print(resp)

    async def get_termins_text(self, category_of_termins_id: int | str, locale: str):
        pass

    async def parse_stadburo(self, category_of_termins_id: int | str):
        pass


"""

async with aiohttp.ClientSession() as session:

async with session.post(FIRST_SERVICE_URL, json={"username_status": result, 'username': username}) as resp:

"""

