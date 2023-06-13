import sqlite3


def create_table():
    connection = sqlite3.connect("Rechner.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS rechnungen (id INTEGER PRIMARY KEY AUTOINCREMENT, Resultat FLOAT)")
    connection.commit()

    connection.close()


def fetch_results():
    connection = sqlite3.connect("Rechner.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM rechnungen")
    results = cursor.fetchall()

    connection.close()

    return results


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
        print("Fehler: Division durch Null ist nicht erlaubt!")
        return None


def is_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False


def is_valid_number_of_values(input_str):
    return input_str.isdigit()


def rechner():
    while True:
        while True:
            zahl_count_str = input("Geben Sie die Anzahl der Zahlen ein, mit denen Sie rechnen möchten: ")
            if is_valid_number_of_values(zahl_count_str):
                num_count = int(zahl_count_str)
                if num_count >= 2:
                    break
                else:
                    print("Fehler: Sie müssen mindestens 2 Zahlen angeben!")
            else:
                print("Fehler: Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.")

        zahlen = []
        for i in range(num_count):
            while True:
                zahl_str = input(f"Geben Sie Zahl {i+1} ein: ")
                if is_number(zahl_str):
                    num = float(zahl_str)
                    zahlen.append(num)
                    break
                else:
                    print("✘ Fehler: Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")

        valid_operations = ["+", "-", "*", "/"]

        while True:
            operation = input("Welche Operation möchten Sie durchführen (+, -, *, /)?: ")
            if operation in valid_operations:
                break
            else:
                print("✘ Fehler: Ungültige Operation! Bitte wählen Sie eine der folgenden Optionen: '+', '-', '*', '/'")

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
                    print("✘ Fehler: Division durch Null ist nicht erlaubt!")
                    resultat = None
                    break
                else:
                    resultat = divide(resultat, zahlen[i])
        else:
            print("✘ Fehler: Ungültige Operation!")

        if resultat is not None:
            print("Ergebnis:", resultat)

            connection = sqlite3.connect("Rechner.db")
            cursor = connection.cursor()

            cursor.execute("INSERT INTO rechnungen (Resultat) VALUES (?)", (resultat,))
            connection.commit()

            last_insert_id = cursor.lastrowid
            print("Eingefügte ID:", last_insert_id)

            connection.close()

        repeat = input("Möchten Sie eine weitere Berechnung durchführen? (ja/nein): ")
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
