
print("Wie viel Personen werden ubernachten?")
anzahl_personen = int(input())

print("Wie viel Nächte möchten Sie bleiben?")
anzahl_nächte = int(input())

zimmerpreis = 70

netto_preis = zimmerpreis*anzahl_nächte*anzahl_personen
gesamtpreis = (netto_preis*0.19)+netto_preis
brutto_betrag = gesamtpreis+127

print(f" Die Gesamtpresi für {anzahl_personen} Personen und für {anzahl_nächte} Nächte ist{gesamtpreis: .2f} $ \n Und Bruttobetrag ist {brutto_betrag: .2f} $")