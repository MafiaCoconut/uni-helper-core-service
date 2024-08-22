from aiogram.fsm.state import StatesGroup, State


class GetPersonById(StatesGroup):
    last_help_message_id = State()
