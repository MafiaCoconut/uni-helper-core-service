from application.interfaces.web_interface import WebInterface
import aiohttp

CANTEENMICROSVCRPORT=8001


class WebInterfaceImpl(WebInterface):
    def get_canteens_menu(self, canteen_id: int | str, locale: str):
        async with (aiohttp.ClientSession() as session):
            async with session.get(
                    f"localhost/canteens_menu/{canteen_id}",
                    json={'locale': locale}
            ) as resp:
                print(resp)

    def get_canteens_info(self, canteen_id: int | str, locale: str):
        async with (aiohttp.ClientSession() as session):
            async with session.get(
                    f"localhost/canteens/{canteen_id}",
                    json={'locale': locale}
            ) as resp:
                print(resp)

    def parse_canteen(self,  canteen_id: int | str):
        async with (aiohttp.ClientSession() as session):
            async with session.get(
                    f"localhost/parser/{canteen_id}"
            ) as resp:
                print(resp)

    def parse_canteen_all(self):
        async with (aiohttp.ClientSession() as session):
            async with session.get(
                    f"localhost/parser/all"
            ) as resp:
                print(resp)

    def get_termins_text(self, category_of_termins_id: int | str, locale: str):
        pass

    def parse_stadburo(self, category_of_termins_id: int | str):
        pass


"""

async with aiohttp.ClientSession() as session:

async with session.post(FIRST_SERVICE_URL, json={"username_status": result, 'username': username}) as resp:

"""

