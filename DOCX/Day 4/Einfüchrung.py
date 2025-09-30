#Deklaration

umschueler = "Hallo Welt!" #Python macht automatisch Initialisiet variabel. In diese Fall hat Python die Variable umschueler initialisiert als string

a = 10
b = 5
c = a/b
print(c)

print(10/3)
print(f"{a/b}")
print("Das Ergebnis ist: ", a/b)

c = a%b #Modulo
print(c)

schueler="Marcel"
schueler1="Mostafa"
schueler2="Hamit"
schueler3="Brüning"

#Python rechnen von 0
#            0         1       2       3       4
schueler=["Marsel","Mostafa","Hamit","Brüning", 10]

print(schueler)

schueler.pop() #löscht den lezten Eintrag in der liste
print(schueler)

schueler.pop(1) #löscht den (1) Eintrag in der liste
print(schueler)

schueler.append("Graf") # #fügt einen Eintrag am Ende der Liste hinzu
print(schueler)

print(len(schueler)) #gibt die Länge der Liste zurück

print(schueler[2]) #gibt den Eintrag an der Stelle 2 zurück

#_________________________________________________________

print("Operatoren" \
"." \
"."
".")
a=2
b=3

istkorrekt=a==b #entweder true oder false

print(istkorrekt)

c=3
d=3

istkorrekt=c>=d #entweder true oder false

print(istkorrekt)

#_________________________________________________________

print("AND Operaotr...")
istaufgestanden = True
hatsichangezogen = True
#hat gefruehstueckt = False

perfektgestartet = istaufgestanden and hatsichangezogen #AND Operator
print(perfektgestartet)

#Wenn alle False

istaufgestanden = False
hatsichangezogen = False
#hat gefruehstueckt = False

perfektgestartet = istaufgestanden and hatsichangezogen #AND Operator
print(perfektgestartet)


istaufgestanden = False
hatsichangezogen = False
hatgefruehstueckt = True

if istaufgestanden and hatsichangezogen or hatgefruehstueckt:
    print("Jetzt habe ich meine Zähne geputzt und gefruehstuckt")

else:
    print ("Wacht auf!")
