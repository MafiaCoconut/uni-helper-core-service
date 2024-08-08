from abc import ABC, abstractmethod


class StadburoGateway(ABC):
    @abstractmethod
    async def parse_stadburo(self, category_of_termins_id: int):
        pass

    @abstractmethod
    async def parse_stadburo_all(self):
        pass

    @abstractmethod
    async def get_category_of_termins_data(self, category_of_termins_id: int):
        pass
