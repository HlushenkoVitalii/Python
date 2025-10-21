print("Bitte gebe irgendein Text ein")
eingabe = input()

print(f" Das hier war deine Eingabe {eingabe}")

eingabe1 = int(input("Diese Zahl werde ich addieren: "))
eingabe2 = int(input("Diese zweite Zahl werde ich mit der ersten Eingabe addieren: "))

gesamten_ergebnis = eingabe1+eingabe2

print("Datentyp des Ergebnisses:", type((gesamten_ergebnis)))
print(f"Das Ergebnis laut {gesamten_ergebnis}")