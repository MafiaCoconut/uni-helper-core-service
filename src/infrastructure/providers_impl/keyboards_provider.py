from application.providers.keyboards_provider import KeyboardsProvider
from application.telegram.keyboards.admin_keyboards import AdminKeyboardsBuilder
from application.telegram.keyboards.authorization_keyboards import AuthorizationKeyboardsBuilder
from application.telegram.keyboards.canteens_keyboards import CanteensKeyboardsBuilder
from application.telegram.keyboards.links_keyboards import LinksKeyboardsBuilder
from application.telegram.keyboards.menu_main_keyboards import MenuMainKeyboardsBuilder
from application.telegram.keyboards.navigator_keyboards import NavigatorKeyboardsBuilder
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from application.telegram.keyboards.stadburo_keyboards import StadburoKeyboardsBuilder


class KeyboardsProviderImpl(KeyboardsProvider):
    def __init__(self,
                 canteens_keyboards: CanteensKeyboardsBuilder,
                 stadburo_keyboards: StadburoKeyboardsBuilder,
                 settings_keyboards: SettingsKeyboardsBuilder,
                 navigator_keyboards: NavigatorKeyboardsBuilder,
                 links_keyboards: LinksKeyboardsBuilder,
                 menu_main_keyboards: MenuMainKeyboardsBuilder,
                 authorization_keyboards: AuthorizationKeyboardsBuilder,
                 admin_keyboards: AdminKeyboardsBuilder,
                 ):
        self.canteens_keyboards = canteens_keyboards
        self.stadburo_keyboards = stadburo_keyboards
        self.settings_keyboards = settings_keyboards
        self.navigator_keyboards = navigator_keyboards
        self.links_keyboards = links_keyboards
        self.menu_main_keyboards = menu_main_keyboards
        self.authorization_keyboards = authorization_keyboards
        self.admin_keyboards = admin_keyboards

    def get_canteens_keyboards(self) -> CanteensKeyboardsBuilder:
        return self.canteens_keyboards

    def get_stadburo_keyboards(self) -> StadburoKeyboardsBuilder:
        return self.stadburo_keyboards

    def get_settings_keyboards(self) -> SettingsKeyboardsBuilder:
        return self.settings_keyboards

    def get_navigator_keyboards(self) -> NavigatorKeyboardsBuilder:
        return self.navigator_keyboards

    def get_links_keyboards(self) -> LinksKeyboardsBuilder:
        return self.links_keyboards

    def get_menu_main_keyboards(self) -> MenuMainKeyboardsBuilder:
        return self.menu_main_keyboards

    def get_authorization_keyboards(self) -> AuthorizationKeyboardsBuilder:
        return self.authorization_keyboards

    def get_admin_keyboards(self) -> AdminKeyboardsBuilder:
        return self.admin_keyboards


