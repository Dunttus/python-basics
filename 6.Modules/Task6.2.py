# -*- coding: cp1252 -*-
import random

tasapelit = 0
haviot = 0
voitot = 0
kierros = 0


while True:
    lukuarvo = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa):")

    if lukuarvo == "Jalka":
        luku = random.randint(1,3)
        print("Sin� valitsit:", lukuarvo)
        if luku == 1:
            print("tietokone valitsi: Jalka")
            print("Tasapeli!")
            kierros += 1
            tasapelit += 1
        elif luku == 2:
            print("tietokone valitsi: Ydinase")
            print("H�visit!")
            kierros += 1
            haviot += 1
        else:
            print("tietokone valitsi: Torakka")
            print("Voitit!")
            kierros += 1
            voitot += 1
            
    elif lukuarvo == "Ydinase":
        luku = random.randint(1,3)
        print("Sin� valitsit:", lukuarvo)
        if luku == 1:
            print("tietokone valitsi: Jalka")
            print("Voitit!")
            kierros += 1
            voitot += 1
        elif luku == 2:
            print("tietokone valitsi: Ydinase")
            print("Tasapeli!")
            kierros += 1
            tasapelit += 1
        else:
            print("tietokone valitsi: Torakka")
            print("H�visit!")
            kierros += 1
            haviot += 1
            
    elif lukuarvo == "Torakka":
        luku = random.randint(1,3)
        print("Sin� valitsit:", lukuarvo)
        if luku == 1:
            print("tietokone valitsi: Jalka")
            print("H�visit!")
            kierros += 1
            haviot += 1
        elif luku == 2:
            print("tietokone valitsi: Ydinase")
            print("Voitit!")
            kierros += 1
            voitot += 1
        else:
            print("tietokone valitsi: Torakka")
            print("Tasapeli!")
            kierros += 1
            tasapelit += 1
            
    elif lukuarvo == "Lopeta":
        print("Pelasit",kierros,"kierrosta, joista voitit",voitot,"ja pelasit tasan",tasapelit,"peli�.")
        break
    else:
        print("")
