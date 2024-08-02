from application.telegram.keyboards.settings_keyboards import SettingsKeyboardsBuilder


class SettingsService:
    def __init__(self,
                 settings_keyboards: SettingsKeyboardsBuilder
                 ):
        self.settings_keyboards = settings_keyboards
        self.update_user_data_use_case = UpdateUserDataUseCase()

    def set_new_locale(self, user_id: int, new_locale: str):
