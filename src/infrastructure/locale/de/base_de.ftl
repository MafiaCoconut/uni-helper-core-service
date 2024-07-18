# Welcome message
welcome-message =
    Hallo! 👋 Das ist dein persönlicher Helfer. Hier ist, was er für dich tun kann:

    1. 🍽 <b>Speisekarte:</b> Du kannst das aktuelle Mensa-Menü erhalten, um immer über die Angebote für heute informiert zu sein.

    2. 📬 <b>Menü-Mailing:</b> Holen Sie sich ein tägliches Menü aus dem von Ihnen gewählten Mensa.

    3. 📅 <b>Terminvereinbarung in Stadtbüro:</b> Überprüfe einfach die verfügbaren Termine in Stadbüro.

    4. 🔗 <b>Links:</b> Erhalten Sie schnellen Zugriff auf nützliche Links zu Websites der Universität und mehr.

    Bitte wählen Sie Ihre bevorzugte Sprache für den Bot, indem Sie die entsprechenden Flaggen auswählen.

    Klicken Sie dann auf die Schaltfläche unten, um das Esszimmer auszuwählen, in dem Sie das Menü erhalten.

    Verwende einfach das Hauptmenü zur Navigation. Wenn du Fragen hast, mailst du mir @MafiaCoconut und ich versuche zu helfen!

reactivating-the-bot = Sie haben Bot bereits aktiviert!


# Menü
menu-main =
    <b>Hauptmenü</b>

    Wählen Sie einen Menüpunkt aus.

menu-canteens =
    <b>Mensen</b>

    Wählen Sie die Mensa aus, um die Speisekarte zu erhalten.

menu-links =
    <b>Links</b>

    Wählen Sie einen Menüpunkt aus, um dem Link zu folgen.

menu-stadburo =
    <b>Stadbüro</b>

    Wählen Sie einen Menüpunkt aus, um die Liste der verfügbaren Termine zu erhalten.

menu-immigration =
    <b>Ausländerbehörde</b>

     Wählen Sie einen Menüpunkt aus, um die Liste der verfügbaren Termine zu erhalten.

menu-settings-heading = <b>Liste der verfügbaren Einstellungen für Mensa:</b>
menu-settings-mailing-on = Mailing - aktiviert
menu-settings-mailing-off = Mailing - deaktiviert
menu-settings-mailing-time = Zeit der Mailing - {$mailing_time}
menu-settings-mailing-numbers-on = Anzeige der Kennzeichnungen - aktiviert
menu-settings-mailing-numbers-off = Anzeige der Kennzeichnungen - deaktiviert
menu-settings-canteen = Mensa - {$canteen}
menu-settings-ending = Klicken Sie auf die Schaltfläche, um Ihre Einstellungen zu ändern.

menu-donations =
    Falls Sie den Autor untertützen möchten, können Sie eine Donation auf eine der folgenden Arten machen:

    PayPal: https://www.paypal.me/mafiacoconut

    Bitcoin: `195PiHUBkeAHN8z4ZwMmMPFc9eRbjZUcc2`

menu-additionally =
    <b>Zusäztzich</b>

    Wählen Sie einen Menüpunkt aus.

menu-manuals =
    <b>Anweisungen</b>

    Wählen Sie eine Anweisung aus, um der folgenden Anweisung aufzurufen.

menu-feedback =
    <b>Feedback</b>

    Wählen Sie einen Menüpunkt aus.

menu-contacts =
    🤖 <b>Über den Entwickler</b>

    Hallo! Ich bin @MafiaCoconut, Entwickler von diesem Bot. Ich hoffe, dass er Ihnen Nutzen und Freude bringt!

    📧 <b>Kontakt:</b>
    - Email: mafiacoconut.contacts@gmail.com

    🌐 <b>Links:</b>
    - https://linktr.ee/mafiacoconut


# Tastatur
#Hauptmenü
main-menu-canteen = Mensen
main-menu-links = Links
main-menu-stadburo = Stadbüro
main-menu-settings = Einstellungen
main-menu-donation = Donation
main-menu-additionally = Zusätzlich

# Links
others-links = Andere Links
main-links = Zurück
freebies = Gratis

# Einstellungen
change-mailing-time = Zeit des Mensa-Mailings
change-status-mailing = Mensa-Mailing ein/aus
change-status-numbers-in-menu = Anzeige der Kennzeichnungen ein/aus

#Optionales Menü
menu-manuals-button = Anweisungen
menu-feedback-button = Feedback

#Feedback
contacts = Kontakt
response = Rückmeldung/Beschwerde

# Überleitung
to-menu-main = Zum Hauptmenü
open-menu-main = Hauptmenü öffnen
back = Zurück


# Mensen (innere)
dishes =
    Mensa-Speisekarte <b>{$canteen_name}</b>
    Letzte Aktualisierung: {$day} - {$time_last_parser}


main-dishes-title = <u><b>Hauptgerichte</b></u>

beilagen-title = <u><b>Beilagen</b></u>

no-menu-for-today =
    Speisekarte <b>{$canteen_name}</b>

    Leider gibt es keine Information über die ausgewählte Mensa.

canteen-is-closed =
    Speisekarte <b>{$canteen_name}</b>
    Die ausgewählte Mensa ist zurzeit geschlossen.

canteens-open-time = Essenausgabezeiten <b>{$canteen_name}</b>:

colibri-open-time =
    Speisekarte <b>CoLibri</b> ist nicht verfügbar.

    Öffnungszeiten:

# Stadbüro (innere)
list-of-all-termins = Liste der verfügbaren Termine in <b>{$termins_name}</b> um {$time} {$day_last_activate}:

lack-of-terms = Leider sind keine Termine verfügbar :(

# Einstellungen (innere)
enter-appropriate-time-for-your-daily-mailing =
    Geben Sie die für das Mailing passende Zeit ein.
    Eingabeformat: <b>hh:mm</b>

cancel-button = Klicken Sie auf "Zurück", um abzubrechen.

try-again = Versuchen Sie die Eingabe erneut.

change-mailing-canceled = Die Mailingzeitänderung wurde abgebrochen.

change-mailing-complete = Die Mailingzeit wurde erofolgreich auf <b>{$time}</b> geändert.

# Feedback
heading-to-send-to-developer = Geben Sie den Text ein, den Sie an den Entwickler senden möchten.

text-to-send-to-developer =
    Sind Sie sicher, dass Sie diese Nachricht senden möchten:
    <b>{$feedback}</b>

    Um eine Nachricht zu senden, klicken Sie auf "Senden"
    Um eine Nachricht zu bearbeiten, klicken Sie auf "Bearbeiten"
    Um eine Nachricht abzubrechen, klicken Sie auf "Abbrechen"

send = Senden
change = Bearbeiten
cancel = Abbrechen

email-successfully-delivered = Nachricht wurde erfolgreich gesendet.

delivery-canceled = Sendung von Feedback/Beschwerde wurde erfolgreich storniert.

echo =
    Kein verfügbarer Befehl auf Anfrage.
    Versuchen Sie es erneut.

in-development = In der Entwicklung

change-canteen = Speisekarte für den Mailing ändern

to-change-canteen = Zur Auswahl der Mensa gehen

disable-mailing-canteen = Die Versendung von Speisekarte deaktivieren

save = Speichern

choose-canteen-for-mailing = Wählen Sie die Mensa aus, deren Mailing Sie erhalten möchten.
is-sure-to-save-canteen = Sie sind sicher, dass Sie {$canteen} wählen möchten?
is-sure-to-disable-mailing-canteen = Sind Sie sicher, dass Sie das Versendung von Speisekarte deaktivieren möchten?