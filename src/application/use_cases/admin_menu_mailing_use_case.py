from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from application.interfaces.telegram_interface import TelegramInterface
from application.telegram.keyboards.admin_menu_keyboards import AdminMenuKeyboardsBuilder
from application.telegram.models.states import SetAdminMailingMessage
from application.use_cases.send_admins_mailing_text_use_case import SendAdminsMailingTextUseCase
from infrastructure.config.logs_config import log_decorator


class AdminMenuMailingUseCase:
    def __init__(
            self,
            telegram_interface: TelegramInterface,
            admin_menu_keyboards: AdminMenuKeyboardsBuilder,
            send_admins_mailing_text_use_case: SendAdminsMailingTextUseCase
    ):
        self.telegram_interface = telegram_interface
        self.admin_menu_keyboards = admin_menu_keyboards
        self.send_admins_mailing_text_use_case = send_admins_mailing_text_use_case

    @log_decorator(print_args=False, print_kwargs=False)
    async def menu_mailing(self, callback):
        await self.telegram_interface.edit_message_with_callback(
            callback,
            message="Меню рассылки",
            keyboard=await self.admin_menu_keyboards.menu_mailing()
        )

    @log_decorator(print_args=False, print_kwargs=False)
    async def menu_get_mailing_text(self, callback, state: FSMContext):
        message_id = await self.telegram_interface.edit_message_with_callback(
            callback,
            message="Отправьте текст для отправки",
            keyboard=await self.admin_menu_keyboards.menu_get_mailing_text()
        )

        await state.update_data(last_message_id=message_id)

        await state.set_state(SetAdminMailingMessage.set_message)

    @log_decorator(print_args=False, print_kwargs=False)
    async def menu_refactor_mailing_text_after_message(self, message: Message, state: FSMContext, mailing_text: str):
        state_data = await state.get_data()
        last_message_id = state_data.get("last_message_id")

        await state.update_data(mailing_text=mailing_text)
        await state.set_state()

        await self.telegram_interface.edit_message(
            chat_id=message.chat.id,
            message_id=last_message_id,
            message=f"Ваше сообщение:\n\n {mailing_text}",
            keyboard=await self.admin_menu_keyboards.menu_refactor_mailing_text(),
            parse_mode=ParseMode.MARKDOWN
        )
    @log_decorator(print_args=False, print_kwargs=False)
    async def menu_refactor_mailing_text_after_callback(self, callback: CallbackQuery, state: FSMContext):
        state_data = await state.get_data()
        mailing_text = state_data.get("mailing_text")

        await self.telegram_interface.edit_message_with_callback(
            callback,
            message=f"Ваше сообщение:\n\n {mailing_text}",
            keyboard=await self.admin_menu_keyboards.menu_refactor_mailing_text(),
            parse_mode=ParseMode.MARKDOWN
        )

    @log_decorator(print_args=False, print_kwargs=False)
    async def menu_check_send_mailing_text(self, callback: CallbackQuery, state: FSMContext):
        state_data = await state.get_data()
        mailing_text = state_data.get("mailing_text")

        await self.telegram_interface.edit_message_with_callback(
            callback,
            message=f"Вы уверены что хотите отправить это сообщение?\n\n{mailing_text}",
            keyboard=await self.admin_menu_keyboards.menu_mailing_check_send_mailing(),
            parse_mode=ParseMode.MARKDOWN
        )

    @log_decorator(print_args=False, print_kwargs=False)
    async def send_admin_mailing_text(self, callback: CallbackQuery, state: FSMContext):
        state_data = await state.get_data()
        mailing_text = state_data.get("mailing_text")

        await self.telegram_interface.edit_message_with_callback(
            callback,
            message="Сообщение отправлено активным пользователям",
            keyboard=await self.admin_menu_keyboards.menu_main()
        )

        await self.send_admins_mailing_text_use_case.execute(mailing_text=mailing_text)
















