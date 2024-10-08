from icecream import ic

from application.gateways.stadburo_gateway import StadburoGateway
from application.services.translation_service import TranslationService
from application.use_cases.generate_termins_list_use_case import GenerateTerminsListUseCase
from application.use_cases.refactor_stadburo_termins_to_text_use_case import RefactorStadburoTerminsToTextUseCase
from infrastructure.config.logs_config import log_decorator


class StadburoService:
    def __init__(self,
                 stadburo_gateway: StadburoGateway,
                 translation_service: TranslationService,
                 ):
        self.stadburo_gateway = stadburo_gateway
        self.translation_service = translation_service
        self.generate_termins_list_use_case = GenerateTerminsListUseCase(
            stadburo_gateway=stadburo_gateway,
            translation_service=translation_service
        )

    async def get_termins_text(self, category_id: int, locale: str) -> str:
        """
        Функция возвращает текст терминов выбранной столовой на выбранном языке
        :param category_id: ID столовой в базе данных
        :param locale: Языковая локаль
        :return: Текст со списком терминов категории
        """
        return await self.generate_termins_list_use_case.execute(category_of_termins_id=category_id, locale=locale)

    async def parse_category(self, category_id: str):
        pass

    async def parse_all(self):
        pass