import logging


system_logger = logging.getLogger("system_logger")
user_logger = logging.getLogger("user_logger")
error_logger = logging.getLogger("error_logger")


class LogsHandler:
    @staticmethod
    def set_func(function: str, status: str = "info"):
        """
        Функция сохраняет лог о вызове функции

        :param str function: Название функции
        :param str status: Тип лога

        :return: None
        """
        result = f"Called Function:({function})"
        if status == "info":
            system_logger.info(result)
        elif status == "debug":
            system_logger.debug(result)

    @staticmethod
    def set_inside_func(function: str, data: str, status: str = "info"):
        """
        Функция выводит информацию о логе внутри конкретной функции

        :param str function: Название функции
        :param str data: Информация, которую нужно сохранить
        :param str status: Тип лога

        :return: None
        """
        # result = f"[{tag}] [{function}]: {data}"
        result = f"[{function}]: {data}"
        if status == "info":
            system_logger.info(result)
        elif status == "debug":
            system_logger.debug(result)
        elif status == "error":
            system_logger.error(result)

    @staticmethod
    def set_func_and_person(function, message, status="info"):
        """
        Функция сохраняет лог о вызове функции и о том, кто её вызвал

        :param str function: Название функции
        :param Message message: Object represents a message from telegram
        :param str status: Название функции

        :return: None
        """
        # result = f"User: {message.chat.username}/{message.chat.id} Tag: [{tag}]  Function: ({function})"
        result = f"User: {message.chat.username}/{message.chat.id} Called function: ({function})"
        if status == "info":
            user_logger.info(result)
            system_logger.info(result)
        elif status == "debug":
            user_logger.debug(result)
            system_logger.debug(result)

    @staticmethod
    def send_log(message):
        """
        Функция выводит сообщение пользователя отправленное без команды

        :param Message message: Object represents a message from telegram

        :return: None
        """
        result = f'User: {message.chat.username}/{message.chat.id} Send Message: "{message.text}"'
        user_logger.info(result)
        system_logger.debug(result)

    @staticmethod
    def add_or_delete_user(message, command):
        """
        Функция выводит сообщение о добавлении или удалении пользователя из бд

        :param Message message: Object represents a message from telegram
        :param str command: Команда удалить или сохранить пользователя

        :return: None
        """
        if command == "add":
            result = f"Add User: {message.chat.username}/{message.chat.id}"
        else:
            result = f"Delete User: {message.chat.username}/{message.chat.id}"

        user_logger.info(result)
        system_logger.info(result)

