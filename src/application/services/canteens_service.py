from icecream import ic

from application.interfaces.web_interface import WebInterface


class CanteensService:
    def __init__(self,
                 web_interface: WebInterface,
                 ):
        self.web_interface = web_interface

    async def get_canteens_menu(self, canteen_id: str | int, locale: str) -> str:
        json_data = await self.web_interface.get_canteens_menu(canteen_id, locale)
        if json_data.get('error').get('type') == "Canteen is now closed":
            return json_data.get('error').get('text')
        else:
            return json_data.get('menu')

    async def get_canteens_info(self, canteen_id: str | int, locale: str) -> str:
        return await self.web_interface.get_canteens_info(canteen_id, locale)

    async def parse_canteen(self, canteen_id: str | int) -> str:
        return await self.web_interface.parse_canteen(canteen_id)

    async def parse_canteen_all(self):
        await self.web_interface.parse_canteen_all()
