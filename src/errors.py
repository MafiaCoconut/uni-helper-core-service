from enum import Enum


class MenuErrorCodes(Enum):
    CANTEEN_IS_CLOSED = 'Canteen is now closed'
    MENU_IS_NONE = 'No dishes in database'


class TerminsErrorCodes(Enum):
    LACK_OF_TERMINS = 'There is no available termins'
