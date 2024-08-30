from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from application.services.translation_service import TranslationService


class LinksKeyboardsBuilder:
    def __init__(self, translation_service: TranslationService):
        self.translation_service = translation_service

    async def get_first_page_links(self, locale: str):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Marvin",
                                         url="https://marvin.uni-marburg.de/qisserver/pages/cs/sys/portal/hisinoneStartPage.faces"),
                    InlineKeyboardButton(text="Ilias",
                                         url="https://ilias.uni-marburg.de/login.php?cmd=force_login"),
                    InlineKeyboardButton(text="Mail",
                                         url="https://home.students.uni-marburg.de/login.php"),
                ],
                [
                    InlineKeyboardButton(text="Mensa Marburg",
                                         url="https://studierendenwerk-marburg.de/essen-trinken/speisekarte/"),
                    InlineKeyboardButton(text="Mensa THM",
                                         url="https://www.stwgi.de/mensa-thm-giessen")

                ],
                [
                    InlineKeyboardButton(text="Marburg Bibliothek",
                                         url="https://arbeitsplatz.ub.uni-marburg.de/index.php?location=gruppen"),
                    InlineKeyboardButton(text="Rückzahlung",
                                         url="https://idp.hebis.de/ub-marburg/Authn/UserPassword"),
                ],
                [
                    InlineKeyboardButton(text="Giessen Bibliothek",
                                         url="https://www.thm.de/bibliothek/lernortplus/raeume-ausstattung/arbeitsplatz-buchungssystem"),
                ],
                [
                    InlineKeyboardButton(text="Stadburo",
                                         url="https://termine-reservieren.de/termine/marburg/")
                ],
                [
                    InlineKeyboardButton(text=await self.translation_service.translate(
                                            message_id='others-links', locale=locale),
                                         callback_data="menu_links_second_page"),

                    InlineKeyboardButton(text=await self.translation_service.translate(
                                            message_id='to-menu-main', locale=locale),
                                         callback_data="menu_main"),
                ],

            ]
        )
        return keyboard

    async def get_second_page_links(self, locale: str):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="WiFi",
                                         url="https://www.uni-marburg.de/de/hrz/dienste/wlan"),
                    InlineKeyboardButton(text="Printer",
                                         url="https://www.uni-marburg.de/de/hrz/dienste/kopieren-drucken-scannen"),
                    InlineKeyboardButton(text="VPN",
                                         url="https://www.uni-marburg.de/de/hrz/dienste/vpn"),
                ],
                [
                    InlineKeyboardButton(text="Deutschland-Ticket",
                                         url="https://weblogin.uni-marburg.de/idp/profile/SAML2/POST/SSO?execution=e1s2"),
                    InlineKeyboardButton(text="Deutsche Radio",
                                         url="https://www.rundfunkbeitrag.de/meldedaten/"),

                    # InlineKeyboardButton(text="Nextbike",
                    #                      url=""),
                ],
                [
                    # InlineKeyboardButton(text=l10n.format_value('freebies'),
                    #                      url="https://medium.com/@alex.kach.2222/халява-c223847b7bcb"),
                    # InlineKeyboardButton(text="Deutsche Ticket",
                    #                      url="https://weblogin.uni-marburg.de/idp/profile/SAML2/POST/SSO?execution=e1s2"),

                    # InlineKeyboardButton(text="Nextbike",
                    #                      url=""),
                ],
                [
                    InlineKeyboardButton(text=await self.translation_service.translate(
                                            message_id='main-links', locale=locale),
                                         callback_data="menu_links_first_page"),

                    InlineKeyboardButton(text=await self.translation_service.translate(
                                            message_id='to-menu-main', locale=locale),
                                         callback_data="menu_main"),
                ]
            ]
        )
        return keyboard
