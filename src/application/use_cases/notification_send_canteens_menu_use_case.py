
class NotificationSendCanteensMenuUseCase:
    def __init__(self,):
        pass

    def execute(self, user_id: int):
        pass

    """
    TODO:
    1. Обращаемся к user api для получения объекта User
    2. Используя указанную для User столовую берём данные об этой столовой через api 
    3. Используя данные Canteen отдаём их классу рефактору данных в текст
    4. Полученный текст отдаём TelegramInterface для отправки конкретному User 
    """