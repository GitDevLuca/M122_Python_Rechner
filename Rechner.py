#Dies is ein kleiner Taschenrechner 🌐

# Funktionen Definieren, Plus, Minus, Mal, Durch
def Addition(x, y):
    return x + y
def Subtraktion(x, y):
    return x - y
def Multiplikation(x, y):
    return x * y
def Division(x, y):
    return x / y


# Inputs vom User für die Berechnung fordern

print("Taschenrechner")



#Hier kann man auswählen welche Operation benutzt werden soll
while True:
    print("Bitte wählen Sie eine Operation aus:")
    print("1. Addieren")
    print("2. Subtraahieren")
    print("3. Multiplizieren")
    print("4. Dividieren")
    print("5. Beenden")

#In dieser Variable wird gespeichert welche eingabe getätigt wurde
    Operation = input("Auswahl: ")
    
    

#Wenn 5 gewählt wird, wird der Taschenrechner gestoppt
    if Operation == '5':
        print("Programm beendet.")
        break

# Hier werden 2 Eingaben vom Benutzer gefordert um jeweils damit zu rechnen
    Eingabe1 = float(input("Gib die erste Zahl ein: "))
    Eingabe2 = float(input("Gib die zweite Zahl ein: "))


#Hier werden die einzelnen berechnungen durchgeführt
    if Operation == "1":
        Resultat = Addition(Eingabe1, Eingabe2)


    elif Operation == "2":
        Resultat = Subtraktion(Eingabe1, Eingabe2)


    elif Operation == "3":
        Resultat = Multiplikation(Eingabe1, Eingabe2)


    elif Operation == "4":
        Resultat = Division(Eingabe1, Eingabe2)


#Anschliessend werden diese in der Variable "Resultat" gespeichert & Hier ausgegeben
    print("Das Ergebnis Ist:", Resultat)
    print("")
