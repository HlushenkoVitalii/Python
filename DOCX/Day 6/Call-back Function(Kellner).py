# call-back function

bestellung = None

def bring_essen(bestellung):
        print("Hier ist Ihre " +bestellung)

def ruf_kellner(bring_essen, bestellung):
        print("Was möchten Sie essen?")
        bestellung = input()
        bring_essen(bestellung)

ruf_kellner(bring_essen, bestellung)