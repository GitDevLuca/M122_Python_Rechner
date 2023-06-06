import sys

def start_from_beginning():
    # Dies ist ein kleiner Taschenrechner 🌐

    # Funktionen definieren: Plus, Minus, Mal, Durch
    def Addition(x, y):
        return x + y

    def Subtraktion(x, y):
        return x - y

    def Multiplikation(x, y):
        return x * y

    def Division(x, y):
        return x / y

    print("Taschenrechner")

    while True:
        print("Bitte wählen Sie eine Operation aus:")
        print("1. Addieren")
        print("2. Subtrahieren")
        print("3. Multiplizieren")
        print("4. Dividieren")
        print("5. Beenden")

        Operation = input("Auswahl: ")

        if Operation not in ["1", "2", "3", "4", "5"]:
            print("Ungültige Eingabe. Bitte wählen Sie eine Zahl von 1-5.")
            continue

        if Operation == '5':
            print("Programm beendet.")
            break

        try:
            Eingabe1 = float(input("Geben Sie die erste Zahl ein: "))
            Eingabe2 = float(input("Geben Sie die zweite Zahl ein: "))
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
            continue

        if Operation == "1":
            Resultat = Addition(Eingabe1, Eingabe2)
        elif Operation == "2":
            Resultat = Subtraktion(Eingabe1, Eingabe2)
        elif Operation == "3":
            Resultat = Multiplikation(Eingabe1, Eingabe2)
        elif Operation == "4":
            if Eingabe2 == 0:
                print("Fehler: Division durch Null ist nicht erlaubt.")
                continue
            Resultat = Division(Eingabe1, Eingabe2)

        print("Das Ergebnis ist:", Resultat)
        print("")



start_from_beginning()
