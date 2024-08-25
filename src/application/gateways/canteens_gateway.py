from abc import ABC, abstractmethod

from domain.entities.canteen import Canteen
from domain.entities.user import User


class CanteensGateway(ABC):
    @abstractmethod
    async def get_canteens_data(self, canteen_id: int):
        """
        Функция обращается к hessen-mensen-parser и возвращает данные о столовой и её меню формате json

        :param canteen_id: Номер столовой в бд
        :return: dict{'canteen': Canteen, 'main_dishes': list[MainDish], 'side_dishes': list[SideDish]}
        """
        pass

    @abstractmethod
    async def get_canteens_info(self, canteen_id: int) -> Canteen:
        pass

    @abstractmethod
    async def parse_canteen(self, canteen_id: int):
        pass

    @abstractmethod
    async def parse_canteen_all(self):
        pass

    @abstractmethod
    async def reactivate(self, canteen_id: int):
        pass

    @abstractmethod
    async def deactivate(self, canteen_id: int):
        pass




