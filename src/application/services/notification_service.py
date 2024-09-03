from application.gateways.notification_gateway import NotificationGateway
from application.use_cases.notification_use_case import NotificationUseCase


class NotificationService:
    def __init__(self,
                 notification_gateway: NotificationGateway,

                 ):
        self.notification_gateway = notification_gateway
        self.notification_use_case = NotificationUseCase(notification_gateway=notification_gateway)


    async def delete_canteens_menu_mailing(self, user_id: int):
        await self.notification_use_case.delete_canteens_menu(user_id=user_id)

    async def set_canteens_menu_mailing(self, user_id: int, mailing_time: str):
        await self.notification_use_case.set_canteens_menu(user_id=user_id, mailing_time=mailing_time)

    async def update_canteens_menu_mailing(self, user_id: int, new_mailing_time: str):
        await self.notification_use_case.update_canteens_menu_mailing(user_id=user_id, new_mailing_time=new_mailing_time)




