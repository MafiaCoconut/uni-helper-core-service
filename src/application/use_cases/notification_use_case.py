from application.gateways.notification_gateway import NotificationGateway


class NotificationUseCase:
    def __init__(self, notification_gateway: NotificationGateway):
        self.notification_gateway = notification_gateway

    def delete_canteens_menu(self, user_id: int):
        self.notification_gateway.delete_canteens_menu_mailing_time(user_id=user_id)

    def set_canteens_menu(self, user_id: int, mailing_time: str):
        self.notification_gateway.set_canteens_menu_mailing_time(user_id=user_id, mailing_time=mailing_time)