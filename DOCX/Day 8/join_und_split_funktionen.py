
studenten = "jörg", "Patrick", "Holger", "Christopher", "Christian"
ausgabe = ", ".join(studenten)
print(studenten)

print(", ".join(studenten))
print(" sind intelegente Menschen ".join(studenten))

print("Das sind meine liebsten Studenten "+str(studenten)+" nicht wahr)")
print("Das sind meine liebsten Studenten {ausgabe}, nicht wahr?")

studenten = "jörg,Patrick,Holger,Christopher,Christian"
print(studenten.split(","))

ergebnis = print(studenten.split(","))
print(ergebnis) # gleich wie fruh

print(type(studenten))

tier = "Wer hat die Gans gestolen"
print(tier.split(" "))
