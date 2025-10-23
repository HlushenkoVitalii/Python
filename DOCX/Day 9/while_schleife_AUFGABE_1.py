
zahlen = []
zahl = 0
wie_viel_zahlen = 0


print("Gibt mir Zahlen und du bekommst Durchschnit, aber nur positive Zahlen!")
zahl = input(f"Einfach schreib: ")
zahl = int(zahl)

while zahl > 0:
    zahlen.append(zahl)
    zahl = input(f"Braucht noch ein Zahl: ")
    zahl = int(zahl)
    if zahl > 0:
        zahlen.append(zahl)
        wie_viel_zahlen = zahlen.count
        durchschnit = sum(zahlen)/wie_viel_zahlen
        print(f"Die Durchschnit ist {durchschnit}")