# Стартовое сообщение
welcome-message =
    Hi! 👋 This is your personal assistant. Here's what it can do for you:

    1. 🍽 <b>Mensa Menu:</b> You can find out the current menu to always be aware of the offers for today.

    2. 📬 <b>Mailing of the menu:</b> Get the daily menu from the dining room of your choice.

    3. 📅 <b>Application in Stadbüro:</b> Easily check the available slots for appointment in Stadbüro.

    4. 🔗 <b>Links:</b> Get quick access to useful links to university websites and more.

    Please select the preferred language of the bot using the appropriate flags.

    Then click the button below to select the dining room where you will receive the menu.

    Just use the main menu to navigate. If you have any questions, write to me @MafiaCoconut and I will try to help!

reactivating-the-bot = You have already activated the bot!


# Menu
menu-main =
    <b>Main menu</b>

    Select a menu item.

menu-canteens =
    <b>Canteens</b>

    Select the canteen to get the menu.

menu-links =
    <b>Links</b>

    Select a menu item to follow the link.

menu-stadburo =
    <b>Stadtbüro</b>

    Select a section to get a list of available Terminen.

menu-immigration =
    <b>Immigration Office</b>

    Select a section to get a list of available Terminen.

menu-settings-heading = <b>List of available settings for Mensa:</b>
menu-settings-mailing-on = Mailing - On
menu-settings-mailing-off = Mailing - Off
menu-settings-mailing-time = Mailing time - {$mailing_time}
menu-settings-mailing-numbers-on = Displaying numbers in the menu - On
menu-settings-mailing-numbers-off = Displaying numbers in the menu - Off
menu-settings-canteen = Canteen - {$canteen}
menu-settings-ending = Click on the button to change settings.

menu-donations =
    If you want to support the author, you can flip a coin in one of the following ways:

    PayPal: https://www.paypal.me/mafiacoconut

    Bitcoin: `195PiHUBkeAHN8z4ZwMmMPFc9eRbjZUcc2`

menu-additionally =
    <b>Additionally</b>

    Select a menu item.

menu-manuals =
    <b>Manuals</b>

    Select the instruction to go to it.

menu-feedback =
    <b>Feedback</b>

    Select a menu item.

menu-contacts =
    🤖 <b>About the developer</b>

    Hi! I am @MafiaCoconut, the developer of this bot. I hope it brings you benefit and pleasure!

    📧 <b>Connection:</b>
    - Email: mafiacoconut.contacts@gmail.com

    🌐 <b>Links:</b>
    - https://linktr.ee/mafiacoconut


# Клавиатура
# Главное меню
main-menu-canteen = Canteens
main-menu-links = Links
main-menu-stadburo = Stadbüro
main-menu-settings = Settings
main-menu-donation = Donation
main-menu-additionally = Additionally

# Ссылки
others-links = Others links
main-links = Back
freebies = Freebies

# Настройки
change-mailing-time = The time of mailing of the menu Mensa
change-status-mailing = Turn on/off the menu Mensa mailing
change-status-numbers-in-menu = Turn on/off numbers in the menu Mensa

#Дополнительное меню
menu-manuals-button = Instructions
menu-feedback-button = Feedback

#Обратная связь
contacts = Contacts
response = Feedback/Complaint

# Перенаправление
to-menu-main = To the main menu
open-menu-main = Open the mein menu
back = Back


# Столовые (внутреннее)
dishes =
    Canteen menu <b>{$canteen_name}</b>
    The time of the last update: {$day} - {$time_last_parser}


main-dishes-title = <u><b>Main dishes</b></u>

beilagen-title = <u><b>Additional dishes</b></u>

no-menu-for-today =
    Canteen menu <b>{$canteen_name}</b>

    Unfortunately, at the moment there is no data on the selected Canteen.

canteen-is-closed =
    Canteen menu <b>{$canteen_name}</b>
    The selected canteen is now closed.

canteens-open-time = Working hours <b>{$canteen_name}</b>:

colibri-open-time =
    Canteen menu <b>CoLibri</b> not available

    Working hours <b>CoLibri</b>:

# Stadburo (внутреннее)
list-of-all-termins = List of available Terminen at the <b>{$termins_name}</b> at {$time} {$day_last_activate}:

lack-of-terms = Unfortunately, there are no available Terminen right now(((

# Settings (внутреннее)
enter-appropriate-time-for-your-daily-mailing =
    Enter the appropriate time for your daily mailing.
    Input format: <b>hh:mm</b>

cancel-button = To cancel, click the "Back" button.

try-again = Please try again.

change-mailing-canceled = The change in the mailing time has been canceled.

change-mailing-complete = The mailing time has been successfully changed to <b>{$time}</b>.

# Feedback
heading-to-send-to-developer = Enter the text you want to send to the developer.

text-to-send-to-developer =
    Are you sure you want to send a message:
    <b>{$feedback}</b>

    To send a message, click "Send"
    To change, click "Edit"
    To cancel sending a message, enter - "Cancel"

send = Send
change = Change
cancel = Cancel

email-successfully-delivered = The message has been successfully delivered.

delivery-canceled = Sending a review/complaint was canceled successfully.

echo =
    There is no command available for your request.
    Please try again.

in-development = In development

change-canteen = Change the canteen for mailing

to-change-canteen = Go to the canteen selection

disable-mailing-canteen = Turn off the mailing

save = Save

choose-canteen-for-mailing = Select the canteen whose mailing you want to receive
is-sure-to-save-canteen = Are you sure you want to choose canteen {$canteen}?
is-sure-to-disable-mailing-canteen = Are you sure you want to disable the mailing of the canteen menus?
