import sqlite3


class colors:
    Green = '\033[92m' #Grün
    WARNING = '\033[93m' #Gelb
    FAIL = '\033[91m' #Rot
    RESET = '\033[0m' #Farbe zurücksetzen
    BOLD = '\033[1m'  # Fett gedruckt

#Der obige Abschnitt importiert das Modul sqlite3 für die Arbeit mit einer SQLite-Datenbank und definiert die Klasse colors,
#die ANSI-Farbsequenzen für die Ausgabe von Text in der Konsole enthält.

def create_table():
    connection = sqlite3.connect("Rechner.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS rechnungen (id INTEGER PRIMARY KEY AUTOINCREMENT, Resultat FLOAT)")
    connection.commit()

    connection.close()

#Die Funktion create_table() erstellt eine Tabelle mit dem Namen "rechnungen" in der SQLite-Datenbank "Rechner.db",
#falls sie noch nicht existiert. Die Tabelle hat zwei Spalten: "id" vom Typ INTEGER als Primärschlüssel und "Resultat" vom Typ FLOAT.

def fetch_results():
    connection = sqlite3.connect("Rechner.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM rechnungen")
    results = cursor.fetchall()

    connection.close()

    return results

#Die Funktion fetch_results() stellt eine Verbindung zur Datenbank her,
#führt eine SELECT-Abfrage aus, um alle Datensätze aus der Tabelle "rechnungen" abzurufen, und gibt die Ergebnisse zurück.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        print(f"{colors.FAIL}Fehler: Division durch Null ist nicht erlaubt!{colors.RESET}")
        return None

#Diese Funktionen führen einfache mathematische Operationen aus und geben das Ergebnis zurück.
#Die Funktion divide() überprüft, ob die Division durch Null vermieden wird und gibt andernfalls eine Fehlermeldung aus.

def is_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False


def is_valid_number_of_values(input_str):
    return input_str.isdigit()

#Diese Hilfsfunktionen überprüfen, ob eine gegebene Zeichenkette eine Zahl bzw. eine gültige Anzahl von Werten ist.

def rechner():
    while True:
        while True:
            zahl_count_str = input(f"{colors.BOLD}Geben Sie die Anzahl der Zahlen ein, mit denen Sie rechnen möchten: {colors.RESET}")
            if is_valid_number_of_values(zahl_count_str):
                num_count = int(zahl_count_str)
                if num_count >= 2:
                    break
                else:
                    print(f"{colors.FAIL}Fehler: Sie müssen mindestens 2 Zahlen angeben!{colors.RESET}")
            else:
                print(f"{colors.FAIL}Fehler: Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.{colors.RESET}")

        zahlen = []
        for i in range(num_count):
            while True:
                zahl_str = input(f"{colors.Green}Geben Sie Zahl {i+1} ein: {colors.RESET}")
                if is_number(zahl_str):
                    num = float(zahl_str)
                    zahlen.append(num)
                    break
                else:
                    print(f"✘{colors.FAIL} Fehler: Ungültige Eingabe! Bitte geben Sie eine Zahl ein.{colors.RESET}")

        valid_operations = ["+", "-", "*", "/"]

        while True:
            operation = input("Welche Operation möchten Sie durchführen (+, -, *, /)?: ")
            if operation in valid_operations:
                break
            else:
                print(f"✘{colors.FAIL}Fehler: Ungültige Operation! Bitte wählen Sie eine der folgenden Optionen: '+', '-', '*', '/'{colors.RESET}")

#In diesem Abschnitt werden die Eingaben des Benutzers für die Anzahl der Zahlen und die Zahlen selbst abgefragt. Die Eingaben werden validiert, um sicherzustellen, dass es sich um gültige Zahlen handelt.
#Anschließend wird der Benutzer nach der gewünschten Operation gefragt, die ebenfalls validiert wird.

        resultat = None

        if operation == "+":
            resultat = zahlen[0]
            for i in range(1, num_count):
                resultat = add(resultat, zahlen[i])
        elif operation == "-":
            resultat = zahlen[0]
            for i in range(1, num_count):
                resultat = subtract(resultat, zahlen[i])
        elif operation == "*":
            resultat = zahlen[0]
            for i in range(1, num_count):
                resultat = multiply(resultat, zahlen[i])
        elif operation == "/":
            resultat = zahlen[0]
            for i in range(1, num_count):
                if zahlen[i] == 0:
                    print(f"{colors.FAIL} ✘ Fehler: Division durch Null ist nicht erlaubt!{colors.RESET}")
                    resultat = None
                    break
                else:
                    resultat = divide(resultat, zahlen[i])
        else:
            print(f"✘{colors.FAIL} Fehler: Ungültige Operation!{colors.RESET}")


#Hier wird die ausgewählte Operation auf die eingegebenen Zahlen angewendet, und das Ergebnis wird in der Variablen resultat gespeichert.
#Dabei werden die entsprechenden mathematischen Funktionen aufgerufen.
#Wenn es sich bei der Division um eine Division durch Null handelt, wird eine Fehlermeldung ausgegeben und das Ergebnis auf None gesetzt.

        if resultat is not None:
            print("Ergebnis:", resultat)

            connection = sqlite3.connect("Rechner.db")
            cursor = connection.cursor()

            cursor.execute("INSERT INTO rechnungen (Resultat) VALUES (?)", (resultat,))
            connection.commit()

            last_insert_id = cursor.lastrowid
            print("Eingefügte ID:", last_insert_id)

            connection.close()


#Hier wird das Ergebnis ausgegeben, sofern es nicht None ist. Es wird eine Verbindung zur Datenbank hergestellt,
#das Ergebnis in die Tabelle "rechnungen" eingefügt und die Verbindung zur Datenbank geschlossen.
#Die ID des letzten eingefügten Datensatzes wird ebenfalls ausgegeben.

        repeat = input(f"{colors.WARNING}Möchten Sie eine weitere Berechnung durchführen? (ja/nein): {colors.RESET}")
        while repeat.lower() != "ja" and repeat.lower() != "nein":
            repeat = input("Bitte geben Sie 'ja' oder 'nein' ein: ")

        if repeat.lower() == "nein":
            break


create_table()
saved_results = fetch_results()
print("Gespeicherte Ergebnisse:")
for result in saved_results:
    if result[1] is not None:
        print(result[1])

rechner()

#Hier wird die create_table()-Funktion aufgerufen, um sicherzustellen, dass die erforderliche Tabelle in der Datenbank vorhanden ist.
#Anschließend werden die gespeicherten Ergebnisse abgerufen und ausgegeben (sofern sie nicht None sind).
#Schließlich wird die Funktion rechner() aufgerufen, um die Benutzerinteraktion zu starten.
