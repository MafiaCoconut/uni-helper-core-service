from fastapi import Depends, APIRouter, Path, Response, status

from application.services.mailing_service import MailingService
from infrastructure.config.services_config import get_mailing_service

router = APIRouter()


@router.post('/notification/canteens_menu/sendCanteensMenu')
async def send_notification_canteens_menu(
        response: Response,
        mailing_service: MailingService = Depends(get_mailing_service)):
    return await mailing_service.send_mailing_canteens_menu()
    # return {'text': "Рассылка выполнена корректно"}


@router.post('/notification/admins_message')
async def send_notification_admins_message():
    return {'text': "Рассылка выполнена корректно"}
