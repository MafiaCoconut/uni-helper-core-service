from fastapi import APIRouter
from infrastructure.config.services_config import canteens_service

router = APIRouter()


@router.post('/notification/canteens_menu/sendCanteensMenu')
async def send_notification_canteens_menu():
    return await canteens_service.send_canteens_menu_to_user()
    # return {'text': "Рассылка выполнена корректно"}


@router.post('/notification/admins_message')
async def send_notification_admins_message():
    return {'text': "Рассылка выполнена корректно"}
