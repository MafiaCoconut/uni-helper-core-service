# Стартовое сообщение
welcome-message =
    Привет! 👋 Это твой личный помощник. Вот что он может для тебя сделать:

    1. 🍽 <b>Меню Mensa:</b> Ты можешь узнать текущее меню, чтобы всегда быть в курсе предложений на сегодня.

    2. 📬 <b>Рассылка меню:</b> Получить ежедневное меню из выбранной тобой столовой.

    3. 📅 <b>Термины в Stadbüro:</b> Легко проверить свободные слоты для записи в Stadbüro.

    4. 🔗 <b>Ссылки:</b> Получить быстрый доступ к полезным ссылкам на сайты университета и не только.

    Пожалуйста, выбери предпочтительный язык бота, используя соответствующие флаги.

    Затем нажми кнопку ниже, для выбора столовой, по которой будешь получать меню.

    Просто используй главное меню для навигации. Если у тебя есть вопросы, напиши мне @MafiaCoconut, и я постараюсь помочь!

reactivating-the-bot = Вы уже активировали бота!


# Меню
menu-main =
    <b>Главное меню</b>

    Выберите пункт меню.

menu-canteens =
    <b>Cтоловые</b>

    Выберите столовую, чтобы получить меню.

menu-links =
    <b>Ссылки</b>

    Выберите пункт меню, чтобы перейти по ссылке.

menu-stadburo =
    <b>Stadtbüro</b>

    Выберите раздел, чтобы получить список доступных терминов.

menu-immigration =
    <b>Иммиграционный офис</b>

    Выберите раздел, чтобы получить список доступных терминов.

menu-settings-heading = <b>Список доступных настроек для Mensa:</b>
menu-settings-mailing-on = Рассылка - Вкл
menu-settings-mailing-off = Рассылка - Выкл
menu-settings-mailing-time = Время рассылки - {$mailing_time}
menu-settings-mailing-numbers-on = Отображение номеров в меню - Вкл
menu-settings-mailing-numbers-off = Отображение номеров в меню - Выкл
menu-settings-canteen = Столовая - {$canteen}
menu-settings-ending = Нажмите на кнопку, чтобы изменить настройки

menu-donations =
    Если вы хотите поддержать автора, можете закинуть монетку одним из нижеперечисленных способов:

    PayPal: https://www.paypal.me/mafiacoconut

    Bitcoin: `195PiHUBkeAHN8z4ZwMmMPFc9eRbjZUcc2`

menu-additionally =
    <b>Дополнительно</b>

    Выберите пункт меню.

menu-manuals =
    <b>Инструкции</b>

    Выберите инструкцию, чтобы перейти к ней.

menu-feedback =
    <b>Обратная связь</b>

    Выберите пункт меню.

menu-contacts =
    🤖 <b>О разработчике</b>

    Привет! Я @MafiaCoconut, разработчик этого бота. Надеюсь, он приносит вам пользу и удовольствие!

    📧 <b>Связь:</b>
    - Email: mafiacoconut.contacts@gmail.com

    🌐 <b>Ссылки:</b>
    - https://linktr.ee/mafiacoconut


# Клавиатура
#Главное меню
main-menu-canteen = Столовые
main-menu-links = Ссылки
main-menu-stadburo = Stadbüro
main-menu-settings = Настройки
main-menu-donation = Пожертвовать
main-menu-additionally = Дополнительно

# Ссылки
others-links = Ещё ссылки
main-links = Вернуться
freebies = Халява

# Настройки
change-mailing-time = Время рассылки меню Mensa
change-status-mailing = Включить/Отключить рассылку меню Mensa
change-status-numbers-in-menu = Включить/Отключить номера в меню Mensa

#Дополнительное меню
menu-manuals-button = Инструкции
menu-feedback-button = Обратная связь

#Обратная связь
contacts = Контакты
response = Отзыв/Жалоба

# Перенаправление
to-menu-main = В главное меню
open-menu-main = Открыть главное меню
back = Назад


# Столовые (внутреннее)
dishes-header =
    Меню столовой <b>{$canteen_name}</b>
    Время последнего обновления: {$day} - {$time_last_parser}


main-dishes-title = <u><b>Основные блюда</b></u>

beilagen-title = <u><b>Дополнительные блюда</b></u>

no-menu-for-today =
    Меню столовой <b>{$canteen_name}</b>

    К сожалению на данный момент данные о выбранной столовой отсутствуют.

canteen-is-closed =
    Меню столовой <b>{$canteen_name}</b>
    Выбранная столовая сейчас закрыта.

canteens-open-time = Время работы <b>{$canteen_name}</b>:

colibri-open-time =
    Меню столовой <b>CoLibri</b> не доступно

    Время работы CoLibri:

# Stadburo (внутреннее)
list-of-all-termins = Список доступных терминов в <b>{$termins_name}</b> на {$time} {$day_last_activate}:

lack-of-terms = К сожалению сейчас нет доступных терминов(((

# Настройки (внутреннее)
enter-appropriate-time-for-your-daily-mailing =
    Введите подходящее для вас время ежедневной рассылки.
    Формат ввода: <b>hh:mm</b>

cancel-button = Для отмены нажмите кнопку "Назад".

try-again = Повторите попытку ввода.

change-mailing-canceled = Изменение времени рассылки отменено.

change-mailing-complete = Время рассылки успешно изменено на <b>{$time}</b>.

# Feedback
heading-to-send-to-developer = Введите текст, который вы хотите отправить разработчику.

text-to-send-to-developer =
    Вы уверены что хотите отправить сообщение:
    <b>{$feedback}</b>

    Для отправки сообщения нажмите - "Отправить"
    Для изменения нажмите "Изменить"
    Для отмены отправки сообщения введите - "Отменить"

send = Отправить
change = Изменить
cancel = Отменить

email-successfully-delivered = Письмо успешно доставлено.

delivery-canceled = Отправка отзыва/жалобы отменена успешно.

echo =
    Нет доступной команды по вашему запросу.
    Повторите попытку.

in-development = В разработке

change-canteen = Изменить столовую для рассылки

to-change-canteen = Перейти к выбору столовой

disable-mailing-canteen = Отключить рассылку

save = Сохранить

choose-canteen-for-mailing = Выберите столовую, рассылку которой хотите получать
is-sure-to-save-canteen = Вы уверены, что хотите выбрать столовую {$canteen}?
is-sure-to-disable-mailing-canteen = Вы уверены, что хотите отключить рассылку меню столовых?
