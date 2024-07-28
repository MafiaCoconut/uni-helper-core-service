from icecream import ic

from application.interfaces.web_interface import WebInterface
from application.services.translation_service import TranslationService
from application.use_cases.generate_termins_list_use_case import GenerateTerminsListUseCase
from application.use_cases.refactor_stadburo_termins_to_text_use_case import RefactorStadburoTerminsToTextUseCase
from infrastructure.config.logs_config import log_decorator


class StadburoService:
    def __init__(self,
                 web_interface: WebInterface,
                 translation_service: TranslationService,
                 ):
        self.web_interface = web_interface
        self.translation_service = translation_service
        self.generate_termins_list_use_case = GenerateTerminsListUseCase(
            web_interface=web_interface,
            translation_service=translation_service
        )

    @log_decorator
    async def get_termins_text(self, category_id: int, locale: str) -> str:
        """
        Функция возвращает текст терминов выбранной столовой на выбранном языке
        :param category_id: ID столовой в базе данных
        :param locale: Языковая локаль
        :return: Текст со списком терминов категории
        """
        return await self.generate_termins_list_use_case.execute(category_of_termins_id=category_id, locale=locale)

    @log_decorator
    async def parse_category(self, category_id: str):
        pass

    @log_decorator
    async def parse_all(self):
        pass