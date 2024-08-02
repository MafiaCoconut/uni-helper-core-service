from abc import ABC, abstractmethod

from domain.entities.user import User


class WebInterface(ABC):
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

    @abstractmethod
    async def get_category_of_termins_data(self, category_of_termins_id: int):
        pass

    @abstractmethod
    async def parse_stadburo(self, category_of_termins_id: int):
        pass

    @abstractmethod
    async def parse_stadburo_all(self):
        pass

    @abstractmethod
    async def create_user(self, user: User):
        pass

    @abstractmethod
    async def update_user_data(
            self,
            user_id: int,
            new_status: str = None,
            new_mailing_time: str = None,
            new_locale: str = None,
            new_canteen_id: int = None,
    ):
        pass

    @abstractmethod
    async def deactivate_user(self, user_id):
        pass

    @abstractmethod
    async def reactivate_user(self, user_id):
        pass

    @abstractmethod
    async def get_users_all(self) -> list[User]:
        pass

    @abstractmethod
    async def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    async def get_users_mailing_time(self, user_id: int) -> str:
        pass

    @abstractmethod
    async def get_users_locale(self, user_id: int) -> str:
        pass

    @abstractmethod
    async def get_users_canteen_id(self, user_id: int) -> int:
        pass

    @abstractmethod
    async def user_check_existence(self, user_id: int) -> bool:
        pass
