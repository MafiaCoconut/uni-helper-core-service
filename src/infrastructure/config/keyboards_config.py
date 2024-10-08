from application.telegram.keyboards.admin_keyboards import AdminKeyboardsBuilder
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder
from application.telegram.keyboards.authorization_keyboards import AuthorizationKeyboardsBuilder
from application.telegram.keyboards.canteens_keyboards import CanteensKeyboardsBuilder
from application.telegram.keyboards.links_keyboards import LinksKeyboardsBuilder
from application.telegram.keyboards.menu_main_keyboards import MenuMainKeyboardsBuilder
from application.telegram.keyboards.navigator_keyboards import NavigatorKeyboardsBuilder
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from application.telegram.keyboards.stadburo_keyboards import StadburoKeyboardsBuilder
from application.telegram.keyboards.translation_keyboards import TranslationKeyboardsBuilder
from infrastructure.config.translation_config import translation_service

canteens_keyboards = CanteensKeyboardsBuilder(translation_service=translation_service)
stadburo_keyboards = StadburoKeyboardsBuilder(translation_service=translation_service)
navigator_keyboards = NavigatorKeyboardsBuilder(translation_service=translation_service)
links_keyboards = LinksKeyboardsBuilder(translation_service=translation_service)
menu_main_keyboards = MenuMainKeyboardsBuilder(translation_service=translation_service)
translation_keyboards = TranslationKeyboardsBuilder()

settings_keyboards = SettingsKeyboardsBuilder(
    translation_service=translation_service,
    translation_keyboards=translation_keyboards,
    navigator_keyboards=navigator_keyboards,
)

authorization_keyboards = AuthorizationKeyboardsBuilder(
    translation_service=translation_service,
    settings_keyboards=settings_keyboards,
    navigator_keyboards=navigator_keyboards,
    translation_keyboards=translation_keyboards
)


admin_keyboards = AdminKeyboardsBuilder(translation_service=translation_service)
admin_menu_keyboards = AdminMenuKeyboardsBuilder()





