from abc import ABC, abstractmethod


class ExcelInterface(ABC):
    @staticmethod
    @abstractmethod
    async def save_to_excel(headers: list, rows: list, path: str):
        pass

    @staticmethod
    @abstractmethod
    async def clear(path: str):
        pass
