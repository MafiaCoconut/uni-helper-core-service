from infrastructure.config.keyboards_config import canteens_keyboards, stadburo_keyboards, settings_keyboards, \
    navigator_keyboards, links_keyboards, menu_main_keyboards, authorization_keyboards, admin_keyboards
from infrastructure.providers_impl.keyboards_provider import KeyboardsProviderImpl

keyboards_provider = KeyboardsProviderImpl(
    canteens_keyboards=canteens_keyboards,
    stadburo_keyboards=stadburo_keyboards,
    settings_keyboards=settings_keyboards,
    navigator_keyboards=navigator_keyboards,
    links_keyboards=links_keyboards,
    menu_main_keyboards=menu_main_keyboards,
    authorization_keyboards=authorization_keyboards,
    admin_keyboards=admin_keyboards,
)
