from abc import ABC, abstractmethod

from application.telegram.keyboards.admin_keyboards import AdminKeyboardsBuilder
from application.telegram.keyboards.authorization_keyboards import AuthorizationKeyboardsBuilder
from application.telegram.keyboards.canteens_keyboards import CanteensKeyboardsBuilder
from application.telegram.keyboards.links_keyboards import LinksKeyboardsBuilder
from application.telegram.keyboards.menu_main_keyboards import MenuMainKeyboardsBuilder
from application.telegram.keyboards.navigator_keyboards import NavigatorKeyboardsBuilder
from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder
from application.telegram.keyboards.stadburo_keyboards import StadburoKeyboardsBuilder


class KeyboardsProvider(ABC):
    @abstractmethod
    def get_canteens_keyboards(self) -> CanteensKeyboardsBuilder:
        pass

    @abstractmethod
    def get_stadburo_keyboards(self) -> StadburoKeyboardsBuilder:
        pass

    @abstractmethod
    def get_settings_keyboards(self) -> SettingsKeyboardsBuilder:
        pass

    @abstractmethod
    def get_navigator_keyboards(self) -> NavigatorKeyboardsBuilder:
        pass

    @abstractmethod
    def get_links_keyboards(self) -> LinksKeyboardsBuilder:
        pass

    @abstractmethod
    def get_menu_main_keyboards(self) -> MenuMainKeyboardsBuilder:
        pass

    @abstractmethod
    def get_authorization_keyboards(self) -> AuthorizationKeyboardsBuilder:
        pass

    @abstractmethod
    def get_admin_keyboards(self) -> AdminKeyboardsBuilder:
        pass

