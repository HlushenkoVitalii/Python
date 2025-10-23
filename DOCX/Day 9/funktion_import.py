
import random

print("Geben sie eine Zahl zwieschen 1 bis 5 ein: ")
input_value = input()

if input_value.isdigit():
    input_value = int(input_value)
    zufallszahl_generator = random.randint(1,5)
    if input_value == zufallszahl_generator:
        print("Herzlichen Glückwunsch du hast gewonnen")
    else:
        print(f"Schade, sie haben verloren, die korrekte Zahl war {zufallszahl_generator}")
else:
    print("Du hast keinen String eingegeben, dass aussieht wie eine Zahl")

print("Danke dass du gespielt hast")