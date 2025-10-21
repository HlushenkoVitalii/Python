
anzahl_äpfeln = 10
anzahl_bananen = 6
anzahl_orangen = 8

preise_apfel = 0.5
preise_banane = 0.3
preise_orange = 0.9

gesamt_preis_äpfeln = anzahl_äpfeln*preise_apfel
gesamt_preis_bananen = anzahl_bananen*preise_banane
gesamt_preis_orangen = anzahl_orangen*preise_orange

gesamt_betrag = gesamt_preis_äpfeln+gesamt_preis_orangen+gesamt_preis_bananen

print(f"Die Gesamtbetrag des Einkauf ist {gesamt_betrag: .2f} $")