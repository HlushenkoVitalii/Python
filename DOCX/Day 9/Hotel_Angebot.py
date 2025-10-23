
zimmerpreis = float(input("Geben Sie den Zimmerpreis pro Person und Nacht ein: "))
aufenthaltdauer = float(input("Geben Sie die Aufenthaltdauer in Nächten ein: "))
anzahl_kind = int(input("Wie viele Kinder hat die Familie zu einchecken: "))

kinderpreis = 0.0
zaehler = 0

while zaehler <anzahl_kind: #zähle ich gleich runter und zaehler
    alter_kinder = int(input(f"Gebe jetzt bitte an, wie alt das Kind ist: {zaehler+1} an "))

    if alter_kinder <=6:
        rabatt = 100
    else:
        rabatt = 50

    kinderpreis+=zimmerpreis*aufenthaltdauer*(1-rabatt/100)
    zaehler +=1

erwachenepreis = 2*zimmerpreis*aufenthaltdauer
gesamtpreis = erwachenepreis+kinderpreis

print("Angebot für diese wunderbare Familie von Herrn Klink")
print(f"\n ZImmerpreis Nacht und Person {zimmerpreis} $ und Aufenthaltsdauer {aufenthaltdauer} in Nächte und Preis für die koplette Familie {gesamtpreis: .2f}")