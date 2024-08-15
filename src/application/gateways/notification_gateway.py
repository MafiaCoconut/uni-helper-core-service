from abc import ABC, abstractmethod


class NotificationGateway(ABC):
    @abstractmethod
    async def update_mailing_time(self, user_id: int, new_mailing_time: str):
        pass

    @abstractmethod
    async def delete_mailing_time(self, user_id: int):
        pass

    @abstractmethod
    async def set_mailing_time(self, user_id: int, mailing_time: str):
        pass
