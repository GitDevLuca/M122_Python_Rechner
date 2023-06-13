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

def calculator():
    while True:
        while True:
            num_count_str = input("Geben Sie die Anzahl der Zahlen ein, mit denen Sie rechnen möchten: ")
            if is_valid_number_of_values(num_count_str):
                num_count = int(num_count_str)
                if num_count >= 2:
                    break
                else:
                    print("Fehler: Sie müssen mindestens 2 Zahlen angeben!")
            else:
                print("Fehler: Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.")

        numbers = []
        for i in range(num_count):
            while True:
                num_str = input(f"Geben Sie Zahl {i+1} ein: ")
                if is_number(num_str):
                    num = float(num_str)
                    numbers.append(num)
                    break
                else:
                    print("Fehler: Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")

        valid_operations = ["+", "-", "*", "/"]

        while True:
            operation = input("Welche Operation möchten Sie durchführen (+, -, *, /)?: ")
            if operation in valid_operations:
                break
            else:
                print("Fehler: Ungültige Operation! Bitte wählen Sie eine der folgenden Optionen: '+', '-', '*', '/'")

        result = None

        if operation == "+":
            result = numbers[0]
            for i in range(1, num_count):
                result = add(result, numbers[i])
        elif operation == "-":
            result = numbers[0]
            for i in range(1, num_count):
                result = subtract(result, numbers[i])
        elif operation == "*":
            result = numbers[0]
            for i in range(1, num_count):
                result = multiply(result, numbers[i])
        elif operation == "/":
            result = numbers[0]
            for i in range(1, num_count):
                if numbers[i] == 0:
                    print("Fehler: Division durch Null ist nicht erlaubt!")
                    result = None
                    break
                else:
                    result = divide(result, numbers[i])
        else:
            print("Fehler: Ungültige Operation!")

        if result is not None:
            print("Ergebnis: ", result)

        repeat = input("Möchten Sie eine weitere Berechnung durchführen? (ja/nein): ")
        while repeat.lower() != "ja" and repeat.lower() != "nein":
            repeat = input("Bitte geben Sie 'ja' oder 'nein' ein: ")

        if repeat.lower() == "nein":
            break

calculator()
