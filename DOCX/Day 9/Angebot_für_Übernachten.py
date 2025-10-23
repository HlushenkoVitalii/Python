
'''
Sreiben Sie ein Programm
    das für eine Familie (zwei Erwachsene und ein Kind) ein Angebot erstellt.
    Kinder von 0 bis 6 Jahren übernachten, kostenlos, ab 7 Jahren auch Erwachsene gibt es einen Rabatt
    von 70% auf den Zimmerpreis pro Person und Nacht

        - Wenn Alter der Kinder kleiner als 7, dann beträgt Rabatt 100%
        - Sonst 70% für alles andere
    Kinderpreis = Zimmerpreis x Aufnthaltdauer x (1-Rabbat/100)

'''
zimmerpreis = float(input("Geben Sie den Zimmerpreis pro Person und Nacht ein: "))
aufenthaltdauer = int(input("Geben Sie die Aufenthaltdauer in Nächten ein: "))
alter_kind = int(input("Gebe bitte das Alter den Kindes ein: "))
rabbat = 0
kinderpreis = 0

if alter_kind<7:
    rabbat = 100
else:
    rabbat = 70

kinderpreis = zimmerpreis*aufenthaltdauer*(1-rabbat/100)

erwachsenenpreis = 2*zimmerpreis*aufenthaltdauer

gesamtpreis = erwachsenenpreis+kinderpreis

print(f"Gesamtpreis für die Familie ist {gesamtpreis}")