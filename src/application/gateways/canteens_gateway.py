from abc import ABC, abstractmethod

from domain.entities.user import User


class CanteensGateway(ABC):
    @abstractmethod
    async def get_canteens_data(self, canteen_id: int):
        pass

    @abstractmethod
    async def get_canteens_info(self, canteen_id: int):
        pass

    @abstractmethod
    async def parse_canteen(self, canteen_id: int):
        pass

    @abstractmethod
    async def parse_canteen_all(self):
        pass



