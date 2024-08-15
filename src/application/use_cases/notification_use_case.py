from application.gateways.notification_gateway import NotificationGateway


class NotificationUseCase:
    def __init__(self, notification_gateway: NotificationGateway):
        self.notification_gateway = notification_gateway

    async def delete_canteens_menu(self, user_id: int):
        await self.notification_gateway.delete_canteens_menu_mailing_time(user_id=user_id)

    async def set_canteens_menu(self, user_id: int, mailing_time: str):
        await self.notification_gateway.set_canteens_menu_mailing_time(user_id=user_id, mailing_time=mailing_time)

    async def update_canteens_menu_mailing(self, user_id: int, new_mailing_time: str):
        await self.notification_gateway.update_mailing_time(user_id=user_id, new_mailing_time=new_mailing_time)



