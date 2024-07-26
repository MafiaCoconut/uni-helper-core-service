from fluent.runtime import FluentLocalization, FluentResourceLoader
from icecream import ic


class TranslationService:
    def __init__(self, status='Production'):
        # self.locales = locales
        # self.loader = FluentResourceLoader("../../infrastructure/locales/{locale}")
        if status == "Production":
            self.loader = FluentResourceLoader("infrastructure/locales/{locale}")
        elif status == "Tests":
            self.loader = FluentResourceLoader("src/infrastructure/locales/{locale}")
        # print(self.loader.localize_path())
        # self.loader.localize_path()
        self.l10n = {
            'en': FluentLocalization(["en"], ["base_en.ftl"], self.loader),
            'ru': FluentLocalization(["ru"], ["base_ru.ftl"], self.loader),
            'uk': FluentLocalization(["uk"], ["base_uk.ftl"], self.loader),
            'de': FluentLocalization(["de"], ["base_de.ftl"], self.loader),
            'ar': FluentLocalization(["ar"], ["base_ar.ftl"], self.loader),
        }

    async def translate(self, message_id: str, locale: str, **kwargs):
        if locale in self.l10n:
            translation = self.l10n[locale].format_value(message_id, kwargs)
            if translation == message_id:
                print(f"Message ID '{message_id}' not found for locale '{locale}'.")
            return translation
        else:
            print(f"Locale '{locale}' not supported.")
            return f"[{message_id}]"

    # def translate(self, message_id: str, locale: str, **kwargs):
    #
    #     print(self.l10n_en.format_value(message_id))
    #     print(self.l10n_de.format_value(message_id))
    #     print(self.l10n_ru.format_value(message_id))
    #     print(self.l10n_uk.format_value(message_id))
    #     self.l10n_en.locales = ['ru']
    #     # self.localization.locales = [locale]
    #     return self.l10n_en.format_value(message_id, kwargs)


if __name__ == "__main__":
    translation_object = TranslationService()
    print(translation_object.translate(message_id="menu-links", locale='ru'))
    print(translation_object.translate(message_id="menu-links", locale='de'))
    print(translation_object.translate(message_id="menu-links", locale='en'))
    print(translation_object.translate(message_id="menu-links", locale='uk'))




#
# # if os.getenv("DEVICE") == "Ubuntu":
# loader = FluentResourceLoader("locales/{locale}")
# # else:
# #     loader = FluentResourceLoader("app/locales/{locale}")
#
# l10n_en = FluentLocalization(["en"], ["base_en.ftl"], loader)
# l10n_ru = FluentLocalization(["ru"], ["base_ru.ftl"], loader)
# l10n_uk = FluentLocalization(["uk"], ["base_uk.ftl"], loader)
# l10n_de = FluentLocalization(["de"], ["base_de.ftl"], loader)
# list_of_available_languages = ['en', 'ru', 'de', 'uk']
#
#
# list_of_l10n = {
#     'ru': l10n_ru,
#     'en': l10n_en,
#     'de': l10n_de,
#     'uk': l10n_uk
# }