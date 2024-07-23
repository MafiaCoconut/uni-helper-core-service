from application.services.translation_service import TranslationService
from domain.entities.canteen import Canteen
from datetime import datetime
from typing import Dict

from domain.entities.main_dish import MainDish
from domain.entities.side_dish import SideDish
from errors import MenuErrorCodes


class RefactorCanteensMenuToTextUseCase:
    def __init__(self,
                 translation_service: TranslationService
                 ):
        self.translation_service = translation_service

    async def execute(
            self,
            canteen: Canteen, main_dishes: list, side_dishes: list,
            locale: str,
            test_time=None, test_day=None
    ) -> dict[str, str]:
        """
        Функция получает данные меню и возвращает текст словарь с возможной ошибкой и текстом для вывода
        :param canteen: Объект столовой
        :param main_dishes: Список объектов MainDish
        :param side_dishes: Список объектов ListDish
        :param locale: Языковая локаль
        :param test_time: Тестовое время получения меню
        :param test_day: Тестовый день получения меню
        :return: {'error': MenuErrorCodes | None, 'text': str}
        """
        result = await self.check_errors(
            canteen=canteen, main_dishes=main_dishes, locale=locale,
            test_time=test_time, test_day=test_day
        )

        if result.get('error') is None:
            result['text'] = await self.set_text(
                canteen=canteen, main_dishes=main_dishes, side_dishes=side_dishes,
                locale=locale
            )

        return result

    async def check_errors(
            self,
            canteen: Canteen, main_dishes: list,
            locale: str,
            test_time=None, test_day=None
    ):
        """
        Функция проверяет работает ли сейчас столовая и есть меню вообще

        :param canteen: Объект столовой
        :param main_dishes: Список объектов MainDish
        :param locale: Языковая локаль
        :param test_time: Тестовое время получения меню
        :param test_day: Тестовый день получения меню
        :return: {'error': MenuErrorCodes | None, 'text': str}
        """
        weekday = int(datetime.now().isoweekday())
        error_text = ""
        error_type = None

        if test_time is not None:
            if not (canteen.opened_time <= test_time <= canteen.closed_time):
                error_type = MenuErrorCodes.CANTEEN_IS_CLOSED
                error_text += await self.translation_service.translate(
                    message_id='canteens-open-time',
                    locale=locale,
                    canteen_name=canteen.name)
                error_text += '\n' + canteen.description

            elif test_day is not None:
                if not (1 <= test_day <= 5):
                    error_type = MenuErrorCodes.CANTEEN_IS_CLOSED
                    error_text += await self.translation_service.translate(
                        message_id='canteens-open-time',
                        locale=locale,
                        canteen_name=canteen.name)
                    error_text += '\n' + canteen.description

        elif not (canteen.opened_time <= datetime.now().hour * 60 + datetime.now().minute <= canteen.closed_time) or \
                not (1 <= weekday <= 5):
            error_type = MenuErrorCodes.CANTEEN_IS_CLOSED
            error_text += await self.translation_service.translate(
                message_id='canteens-open-time',
                locale=locale,
                canteen_name=canteen.name)
            error_text += '\n' + canteen.description

        if not main_dishes:
            error_type = MenuErrorCodes.MENU_IS_NONE
            error_text += await self.translation_service.translate(
                message_id='no-menu-for-today',
                locale=locale,
                canteen_name=canteen.name)
            error_text += '\n\n'
            error_text += await self.translation_service.translate(
                message_id='canteens-open-time',
                locale=locale,
                canteen_name=canteen.name)
            error_text += '\n' + canteen.description

        return {'error': error_type, 'text': error_text}

    async def set_text(
            self,
            canteen: Canteen, main_dishes: list, side_dishes: list,
            locale: str
    ):
        header = await self.get_header(created_at=canteen.created_at, locale=locale, canteen=canteen)
        main_dishes_text = await self.get_main_dishes_text(main_dishes=main_dishes, locale=locale)
        side_dishes_text = await self.get_side_dishes_text(side_dishes=side_dishes, locale=locale)

        return header + main_dishes_text + side_dishes_text

    async def get_header(self, created_at: datetime, locale: str, canteen: Canteen):
        time_parser = created_at
        day = f"{str(time_parser.day).zfill(2)}.{str(time_parser.month).zfill(2)}"
        time_last_parser = f"{str(time_parser.hour).zfill(2)}:{str(time_parser.minute).zfill(2)}"

        text = await self.translation_service.translate(
            message_id='dishes-header',
            locale=locale,
            canteen_name=canteen.name,
            day=day,
            time_last_parser=time_last_parser
        ) + '\n\n\n'
        return text

    async def get_main_dishes_text(self, main_dishes: list, locale: str):
        text = await self.translation_service.translate(
            message_id='main-dishes-title',
            locale=locale) + '\n'

        last_type_of_dish = ""
        for dish in main_dishes:
            if dish.name == "" or dish.name is None or dish.name == " ":
                continue

            dish_text = ""
            if dish.type != last_type_of_dish:
                dish_text += f"<u>{dish.type}</u>\n"
                last_type_of_dish = dish.type

            dish_text += f"* {dish.name}\n"
            if dish.properties != '-':
                dish_text += f"- {dish.properties}\n"
            dish_text += f"= {dish.price}\n\n"

            text += dish_text

        return text

    async def get_side_dishes_text(self, side_dishes: list, locale: str):
        if not side_dishes:
            return ""

        text = await self.translation_service.translate(
            message_id='beilagen-title',
            locale=locale) + '\n'

        for side_dish in side_dishes:
            if side_dish.name == "" or side_dish.name is None or side_dish.name == " ":
                continue
            else:
                # name_dish = side_dish[1]
                # properties = side_dish[2]
                side_dish_text = f"* {side_dish.name}\n"
                if side_dish.properties != '-':
                    side_dish_text += f"- {side_dish.properties}\n"
                if side_dish.price != '-':
                    side_dish_text += f"= {side_dish.price}\n"

                text += side_dish_text + '\n'
        return text
