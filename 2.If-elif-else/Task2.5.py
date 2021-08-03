arvo1 = input("Anna ensimmäinen luku: ")
arvo2 = input("Anna toinen luku: ")
arvo1 = int(arvo1)
arvo2 = int(arvo2)

print("""(1) +
(2) -
(3) *
(4) /""")
arvo3 = input("Tee valinta (1-4): ")

if arvo3 == "1":
    print("Tulos on: ",arvo1+arvo2)
elif arvo3 == "2":
    print("Tulos on: ",arvo1-arvo2)
elif arvo3 == "3":
    print("Tulos on: ",arvo1*arvo2)
elif arvo3 == "4":
    print("Tulos on: ",arvo1/arvo2)
else:
    print("Valintaa ei tunnistettu.")
