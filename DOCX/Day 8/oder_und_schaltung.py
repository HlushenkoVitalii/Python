
# oder und Schaltung

regen = False

bewoelkt = True
#         nein       ja
wetter = regen and bewoelkt
print(wetter)


salat = True
mit_Fleisch = False
mit_Brot = False
mit_Kaese = False

doener = salat or mit_Fleisch or mit_Brot or mit_Kaese # mit OR commt True, weil es gibt eine True
print(doener)

doener = salat and mit_Fleisch and mit_Brot and mit_Kaese # mit AND commt False, weil es gibt eine True und alle andere haben False
print(doener)

doener = salat and