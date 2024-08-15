from application.gateways.notification_gateway import NotificationGateway


class NotificationService:
    def __init__(self,
                 notification_gateway: NotificationGateway,
                 ):
        self.notification_gateway = notification_gateway

    def delete_job(self, user_id: int):
        self.notification_gateway.delete_job(user_id=user_id)

    def set_job(self, user_id: int):
        self.notification_gateway.update_mailing_time(user_id=user_id, new_mailing_time="11:45")
