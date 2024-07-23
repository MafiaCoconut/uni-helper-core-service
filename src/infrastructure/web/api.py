from fastapi import APIRouter


router = APIRouter()


@router.post('/notification/canteens_menu/{user_id}')
async def send_notification_canteens_menu(user_id: int, locale: str):
    return {'text': "Рассылка выполнена корректно"}


@router.post('/notification/admins_message')
async def send_notification_admins_message():
    return {'text': "Рассылка выполнена корректно"}
