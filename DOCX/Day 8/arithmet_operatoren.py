


strom_preis = 0.4

verbrach_tv = 3*1*3*365
verbrach_herd = 4*2*2*52
verbrach_router = 2*4*365
verbrach_heizung = 8*20*170

gesamtverbrach = verbrach_tv + verbrach_herd + verbrach_router + verbrach_heizung
            #0.4
gesamtkosten = strom_preis*gesamtverbrach

print(f"Gesamtkosten des Haushalts im Jahr beträgt {gesamtkosten: .2f}") #empfehlung
print(10/2)
print("Das Ergeblis lautet ", gesamtkosten)



a="7" #string
b=5 #integer

b="5"

print(a+b) #print zeigt 75
print(int(a)+int(b)) #konvertiert oder parsing, print zegt 12

a="3.5"
b="2.9"

print(float(a)/float(b))
print(f"{float(a)/float(b): .2f}")