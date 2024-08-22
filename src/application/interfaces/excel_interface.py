from abc import ABC, abstractmethod


class ExcelInterface(ABC):
    @abstractmethod
    @staticmethod
    async def save_to_excel(headers: list, rows: list, path: str):
        pass

    @abstractmethod
    @staticmethod
    async def clear(path: str):
        pass
