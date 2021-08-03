# -- coding: cp1252 --
jatka = True
luku = 0

while jatka:
    if luku ==0:
        arvo1 = int(input("Anna ensimmäinen luku: "))
        arvo2 = int(input("Anna toinen luku: "))
        luku +=1
    elif luku >= 1:
        arvo1 = int(input("Anna uusi ensimmäinen luku: "))
        arvo2 = int(input("Anna uusi toinen luku: "))
    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Vaihda luvut\n(6)Lopeta")
        print("Valitut luvut:", arvo1, arvo2)
        arvo3 = input("Tee valinta (1-6): ")
        if arvo3 == "1":
            print("Tulos on: ",arvo1+arvo2)
        elif arvo3 == "2":
            print("Tulos on: ",arvo1-arvo2)
        elif arvo3 == "3":
            print("Tulos on: ",arvo1*arvo2)
        elif arvo3 == "4":
            print("Tulos on: ",arvo1/arvo2)
        elif arvo3 == "5":
            break
        elif arvo3 == "6":
            jatka = False
            break
        else:
            print("Valintaa ei tunnistettu.")
