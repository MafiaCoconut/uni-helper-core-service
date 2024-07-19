from abc import ABC, abstractmethod

class WebInterface(ABC):
    @abstractmethod
    async def get_canteens_menu(self, canteen_id: int | str, locale: str):
        pass

    @abstractmethod
    async def get_canteens_info(self, canteen_id: int | str, locale: str):
        pass

    @abstractmethod
    async def parse_canteen(self,  canteen_id: int | str):
        pass

    @abstractmethod
    async def parse_canteen_all(self):
        pass

    @abstractmethod
    async def get_termins_text(self, category_of_termins_id: int | str, locale: str):
        pass

    @abstractmethod
    async def parse_stadburo(self, category_of_termins_id: int | str):
        pass
