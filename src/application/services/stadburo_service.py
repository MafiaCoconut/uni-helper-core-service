from icecream import ic

from application.interfaces.web_interface import WebInterface


class StadburoService:
    def __init__(self,
                 web_interface: WebInterface,
                 ):
        self.web_interface = web_interface

    async def get_termins_text(self, category_id: str | int, locale: str):
        json_data = await self.web_interface.get_termins_text(category_of_termins_id=category_id, locale=locale)
        return json_data.get('text')




    async def parse_category(self, category_id: str):
        pass

    async def parse_all(self):
        pass