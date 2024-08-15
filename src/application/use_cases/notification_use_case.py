from application.gateways.notification_gateway import NotificationGateway


class NotificationUseCase:
    def __init__(self, notification_gateway: NotificationGateway):
        self.notification_gateway = notification_gateway

    def delete_canteens_menu(self, user_id: int):
        self.notification_gateway.delete_job(user_id=user_id)