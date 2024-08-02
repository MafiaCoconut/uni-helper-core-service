from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class TranslationKeyboardsBuilder:
    async def get_locales_list(self, where_was_called: str) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="🇷🇺", callback_data=f'{where_was_called} ru'),
                    InlineKeyboardButton(text="🇺🇦", callback_data=f'{where_was_called} uk'),
                    InlineKeyboardButton(text="🇩🇪", callback_data=f'{where_was_called} de'),
                    InlineKeyboardButton(text="🇺🇸", callback_data=f'{where_was_called} en'),
                    InlineKeyboardButton(text="🇸🇦", callback_data=f'{where_was_called} ar')
                ]
            ]
        )
        return keyboard

