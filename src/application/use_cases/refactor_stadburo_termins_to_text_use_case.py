from application.services.translation_service import TranslationService
from domain.entities.category_of_termin import CategoryOfTermins
from domain.entities.termin import Termin
from errors import TerminsErrorCodes
from infrastructure.config.logs_config import log_decorator


class RefactorStadburoTerminsToTextUseCase:
    def __init__(self,
                 translation_service: TranslationService
                 ):
        self.translation_service = translation_service

    @log_decorator(print_args=False, print_kwargs=False)
    async def execute(self, termins: list[Termin], category_of_termins: CategoryOfTermins, locale: str) -> dict:
        """

        :param termins: Объект списка терминов
        :param category_of_termins: Объект категории терминов
        :param locale: Языковая локаль
        :return: {'error': None|TerminsErrorCodes, 'text': str}
        """
        text = ""
        error = None
        if termins:
            text = await self.translation_service.translate(
                message_id="list-of-all-termins",
                locale=locale,
                termins_name=category_of_termins.name,
                time=termins[0].created_at.strftime("%H:%M"),
                day_last_activate=termins[0].created_at.strftime("%d.%m.%Y")
            ) + "\n\n"

            k = 0
            for i, termin in enumerate(termins):
                k += 1
                if termin.time.day != termins[i-1].time.day:
                    if text[-1] != '\n':
                        text += '\n'
                    text += f"\n<b>{termin.time.strftime('%d.%m.%Y')}</b>\n"
                    k = 1

                text += f"{termin.time.strftime('%H:%M')} "
                if k % 6 == 0:
                    text += '\n'

        else:
            text = await self.translation_service.translate(
                message_id="lack-of-terms",
                locale=locale)
            error = TerminsErrorCodes.LACK_OF_TERMINS

        result = {'text': text, 'error': error}
        return result
