from application.gateways.stadburo_gateway import StadburoGateway
from application.services.translation_service import TranslationService
from application.use_cases.refactor_stadburo_termins_to_text_use_case import RefactorStadburoTerminsToTextUseCase


class GenerateTerminsListUseCase:
    def __init__(self,
                 stadburo_gateway: StadburoGateway,
                 translation_service: TranslationService,
                 ):
        self.stadburo_gateway = stadburo_gateway
        self.refactor_stadburo_termins_to_text_use_case = RefactorStadburoTerminsToTextUseCase(
            translation_service=translation_service
        )

    async def execute(self, category_of_termins_id: int, locale: str) -> str:
        data = await self.stadburo_gateway.get_category_of_termins_data(category_of_termins_id=category_of_termins_id)

        termins = data.get('termins')
        category_of_termins = data.get('category_of_termins')

        result = await self.refactor_stadburo_termins_to_text_use_case.execute(
            termins=termins, category_of_termins=category_of_termins, locale=locale
        )

        if result.get('error') is not None:
            pass
        else:
            return result.get('text')





