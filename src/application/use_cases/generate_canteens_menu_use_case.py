from icecream import ic

from application.interfaces.telegram_interface import TelegramInterface
from application.interfaces.web_interface import WebInterface
from application.services.translation_service import TranslationService
from application.use_cases.refactor_canteens_menu_to_text_use_case import RefactorCanteensMenuToTextUseCase
from application.use_cases.send_canteens_menu_use_case import SendCanteensMenuUseCase
from domain.entities.user import User


class GenerateCanteenMenuUseCase:
    """
    Класс отвечает за преобразование данных Canteen в текст на запрашиваемом языке

    Функции execute получает на вход ID столовой и локаль на которой нужно вернуть текст
    """
    def __init__(self,
                 web_interface: WebInterface,
                 telegram_interface: TelegramInterface,
                 translation_service: TranslationService,
                 ):
        self.web_interface = web_interface
        self.telegram_interface = telegram_interface

        self.translation_service = translation_service
        self.refactor_canteens_menu_to_text_use_case = RefactorCanteensMenuToTextUseCase(
            translation_service=translation_service
        )
        # self.send_canteens_menu_use_case = SendCanteensMenuUseCase(
        #     telegram_interface=telegram_interface
        # )

    async def execute(self, canteen_id: int, locale: str,
                      test_time: int = None, test_day: int = None) -> str:
        """
        Функция преобразует данные Canteen в текст по запрашиваемой локали
        :param canteen_id: ID столовой в базе данных
        :param locale: Языковая локаль
        :param test_day: Ручное указание дня, когда запрашивается столовая
        :param test_time: Ручное указание времени, когда запрашивается столовая
        :return: Текст столовой
        """
        canteen_data = await self.web_interface.get_canteens_data(canteen_id=canteen_id)
        result = await self.refactor_canteens_menu_to_text_use_case.execute(
            main_dishes=canteen_data.get('main_dishes'),
            side_dishes=canteen_data.get('side_dishes'),
            canteen=canteen_data.get('canteen'),
            locale=locale,
            test_day=test_day,
            test_time=test_time,
        )
        ic(result)
        if result.get('error') is None:
            return result.get('text')
        else:
            return result.get('text')
            # TODO сделать реакцию функции если она получила ошибку при попытке собрать текст
            pass



        







"""
Данные отправляются из Notification +
Core получает запрос с user_id +
Core берёт из USERS locale, canteen_id + 
CORE берёт из CANTEENS canteen_name, main_dishes, side_dishes +
CORE создаёт из данных CANTEENS текст
CORE отправляет пользователю созданный текст
"""
