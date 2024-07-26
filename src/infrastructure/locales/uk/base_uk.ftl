# Стартовое сообщение
welcome-message =
    Привіт! 👋 Це твій особистий помічник. Він може для тебе зробити:

    1. 🍽 <b>Меню Mensa:</b> Ти можеш дізнатися поточне меню, щоб завжди бути в курсі щоденних пропозицій.

    2. 📬 <b>Розсилання меню:</b> Отримуй щоденні меню з обраної тобою їдальні.

    3. 📅 <b>Запис у Stadbüro:</b> Легко перевіряй вільні слоти для запису у Stadbüro.

    4. 🔗 <b>Посилання:</b> Отримуй швидкий доступ до корисних посиланнях на сайти університету і не тільки..

    Будь-ласка, вибери бажану мову бота, використовуючи відповідні прапорці.

    Потім натисни кнопку нижче, для вибору їдальні, по якій будеш отримувати меню.

    Просто використовуй головне меню для навігації. Якщо Ти маєш запитання, напиши мені @MafiaCoconut, та я намагатимусь допомогти!

reactivating-the-bot = Ви вже активували бота!


# Меню
menu-main =
    <b>Головне меню</b>

    Вибери пункт меню.

menu-canteens =
    <b>Їдальні</b>

    Вибери їдальню, щоб отримати меню.

menu-links =
    <b>Посилання</b>

    Вибери пункт меню, щоб перейти за посиланням.

menu-stadburo =
    <b>Stadtbüro</b>

    Вибери розділ, щоб отримати перелік доступних термінів.

menu-immigration =
    <b>Імміграційний офіс</b>

    Вибери розділ, щоб отримати перелік доступних термінів.

menu-settings-heading = <b>Перелік доступних налаштувань для Mensa:</b>
menu-settings-mailing-on = Розсилання - Увімк
menu-settings-mailing-off = Розсилання - Вимк
menu-settings-mailing-time = Час розсилання - {$mailing_time}
menu-settings-mailing-numbers-on = Отображение номеров в меню - Увімк
menu-settings-mailing-numbers-off = Отображение номеров в меню - Вимк
menu-settings-canteen = їдальня - {$canteen}
menu-settings-ending = Натисніть на кнопку, щоб змінити налаштування.

menu-donations =
    Якщо ви хочете підтримати автора, можете закинути монетку одним із нижче перелічених способів:

    PayPal: https://www.paypal.me/mafiacoconut

    Bitcoin: `195PiHUBkeAHN8z4ZwMmMPFc9eRbjZUcc2`

menu-additionally =
    <b>Додатково</b>

    Вибери пункт меню.

menu-manuals =
    <b>Інструкції</b>

    Виберіть інструкцію, щоб перейти до неї.

menu-feedback =
    <b>Зворотній зв’язок</b>

    Вибери пункт меню.

menu-contacts =
    🤖 <b>Про розробника</b>

    Привіт! Я @MafiaCoconut, розробник цього бота. Сподіваюся, він приносить вам користь та задоволення!

    📧 <b>Зв’язок:</b>
    - Email: mafiacoconut.contacts@gmail.com

    🌐 <b>Посилання:</b>
    - https://linktr.ee/mafiacoconut


# Клавіатура
#Головне меню
main-menu-canteen = Їдальні
main-menu-links = Посилання
main-menu-stadburo = Stadbüro
main-menu-settings = Налаштування
main-menu-donation = Пожертвувати
main-menu-additionally = Додатково

# Посилання
others-links = Інші посилання
main-links = Повернутися
freebies = Халява

# Налаштування
change-mailing-time = Час розсилання меню Mensa
change-status-mailing = Увімкнути/Вимкнути розсилання меню Mensa
change-status-numbers-in-menu = Увімкнути/Вимкнути номери в меню Mensa

#Додаткове меню
menu-manuals-button = Інструкції
menu-feedback-button = Зворотній зв’язок

#Зворотній зв’язок
contacts = Контакти
response = Відшук/Скарга

# Перенаправлення
to-menu-main = У головне меню
open-menu-main = Відкрити головне меню
back = Назад


# Їдальні (внутрішнє)
dishes-header =
    Меню їдальні <b>{$canteen_name}</b>
    Час останнього оновлення: {$day} - {$time_last_parser}


main-dishes-title = <u><b>Основні страви</b></u>

beilagen-title = <u><b>Додаткові страви</b></u>

no-menu-for-today =
    Меню їдальні <b>{$canteen_name}</b>

    На жаль на даний момент дані про обрану їдальню відсутні.

canteen-is-closed =
    Меню їдальні <b>{$canteen_name}</b>
    Обрана їдальня зараз зачинена.

canteens-open-time = Час роботи <b>{$canteen_name}</b>:

colibri-open-time =
    Меню їдальні <b>CoLibri</b> недоступне

    Час роботи CoLibri:

# Stadburo (внутрішнє)
list-of-all-termins = Перелік вільних термінів у <b>{$termins_name}</b> на {$time} {$day_last_activate}:

lack-of-terms = На жаль зараз немає вільних термінів(((

# Налаштування (внутрішнє)
enter-appropriate-time-for-your-daily-mailing =
    Введіть потрібний для вас час щоденного розсилання
    Формат введення: <b>hh:mm</b>

cancel-button = Щоб скасувати натисніть кнопку “Назад”

try-again = Спробуйте ще раз ввести

change-mailing-canceled = Зміна часу розсилки скасовано

change-mailing-complete = Час розсилання успішно змінено на <b>{$time}</b>

# Feedback
heading-to-send-to-developer = Введіть текст, який ви бажаєте надіслати розробнику

text-to-send-to-developer =
    Ви впевнені, що хочете надіслати повідомлення:
    <b>{$feedback}</b>

    Для надсилання повідомлення натисніть - "Надіслати"
    Щоб змінити натисніть "Змінити"
    Щоб скасувати відправку повідомлення введіть - "Скасувати"

send = Надіслати
change = Змінити
cancel = Скасувати

email-successfully-delivered = Лист успішно доставлений.

delivery-canceled = Надсилання відгука/скарги скасовано успішно.

echo =
    Немає доступної команди на ваш запит.
    Повторіть спробу.

in-development = У розробці

change-canteen = Змінити їдальню для розсилання

to-change-canteen = Перейти до вибору їдальні

disable-mailing-canteen = Вимкнути розсилання

save = Зберегти

choose-canteen-for-mailing = Оберіть їдальню, розсилки якої хочете отримувати
is-sure-to-save-canteen = Ви впевнені, що хочете обрати їдальню {$canteen}?
is-sure-to-disable-mailing-canteen = Ви впевнені, що хочете вимкнути розсилання меню їдалень?
