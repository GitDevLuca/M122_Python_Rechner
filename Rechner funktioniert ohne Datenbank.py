import sqlite3

connection = sqlite3.connect("Rechner.db")

print(connection.total_changes)

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS rechnungen (id INTEGER auto_increment, Resultat FLOAT)")


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

def Rechner():
    while True:
        while True:
            Zahl_count_str = input("Geben Sie die Anzahl der Zahlen ein, mit denen Sie rechnen möchten: ")
            if is_valid_number_of_values(Zahl_count_str):
                num_count = int(Zahl_count_str)
                if num_count >= 2:
                    break
                else:
                    print("Fehler: Sie müssen mindestens 2 Zahlen angeben!")
            else:
                print("Fehler: Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.")

        Zahlen = []
        for i in range(num_count):
            while True:
                Zahl_str = input(f"Geben Sie Zahl {i+1} ein: ")
                if is_number(Zahl_str):
                    num = float(Zahl_str)
                    Zahlen.append(num)
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
            resultat = Zahlen[0]
            for i in range(1, num_count):
                resultat = add(resultat, Zahlen[i])
        elif operation == "-":
            resultat = Zahlen[0]
            for i in range(1, num_count):
                resultat = subtract(resultat, Zahlen[i])
        elif operation == "*":
            resultat = Zahlen[0]
            for i in range(1, num_count):
                resultat = multiply(resultat, Zahlen[i])
        elif operation == "/":
            resultat = Zahlen[0]
            for i in range(1, num_count):
                if Zahlen[i] == 0:
                    print("✘ Fehler: Division durch Null ist nicht erlaubt!")
                    resultat = None
                    break
                else:
                    resultat = divide(resultat, Zahlen[i])
        else:
            print("✘ Fehler: Ungültige Operation!")

        if resultat is not None:
            print("Ergebnis: ", resultat)

            cursor.execute("INSERT INTO rechnungen VALUES (result)")

            connection.commit()

            print(connection.total_changes)

        repeat = input("Möchten Sie eine weitere Berechnung durchführen? (ja/nein): ")
        while repeat.lower() != "ja" and repeat.lower() != "nein":
            repeat = input("Bitte geben Sie 'ja' oder 'nein' ein: ")

        if repeat.lower() == "nein":
            break

Rechner()
