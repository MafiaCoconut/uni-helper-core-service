from icecream import ic

from application.interfaces.web_interface import WebInterface
from application.services.translation_service import TranslationService
from application.use_cases.generate_termins_list_use_case import GenerateTerminsListUseCase
from application.use_cases.refactor_stadburo_termins_to_text_use_case import RefactorStadburoTerminsToTextUseCase


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


    async def get_termins_text(self, category_id: int, locale: str):
        await self.refactor_stadburo_termins_to_text_use_case.execute(category_of_termins=category_id, locale=locale)
        # json_data = await self.web_interface.get_termins_text(category_of_termins_id=category_id, locale=locale)
        # return json_data.get('text')




    async def parse_category(self, category_id: str):
        pass

    async def parse_all(self):
        pass