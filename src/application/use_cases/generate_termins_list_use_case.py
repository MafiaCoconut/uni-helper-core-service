from application.interfaces.web_interface import WebInterface
from application.services.translation_service import TranslationService
from application.use_cases.refactor_stadburo_termins_to_text_use_case import RefactorStadburoTerminsToTextUseCase


class GenerateTerminsListUseCase:
    def __init__(self,
                 web_interface: WebInterface,
                 translation_service: TranslationService,
                 ):
        self.web_interface = web_interface
        self.refactor_stadburo_termins_to_text_use_case = RefactorStadburoTerminsToTextUseCase(
            translation_service=translation_service
        )

    async def execute(self, category_of_termins: int, locale: str):
        result = await self.web_interface.get_category_of_termins_data(category_of_termins)

        termins = result.get('termins')

        await self.refactor_stadburo_termins_to_text_use_case.execute(
            termins=termins, category_of_termins=category_of_termins, locale=locale
        )



