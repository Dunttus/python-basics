# -- coding: cp1252 --


while True:
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4)Lopeta\n")   
    arvo1 = input("Mitä haluat tehdä?: ")
    tiedosto = open("muistio.txt","r")
    sisalto = tiedosto.read()
    
    if arvo1 == "1":      
        print(sisalto)
    elif arvo1 == "2":
        tiedosto.close()
        lukuarvo = input("Kirjoita uusi merkintä:")
        lukuarvo = lukuarvo + "\n"
        tiedosto = open("muistio.txt","a")
        kirjoita = tiedosto.write(lukuarvo)
        tiedosto.close()
    elif arvo1 == "3":
        tiedosto.close()
        tiedosto = open("muistio.txt","w")
        print("Muistio tyhjennetty.")
        tiedosto.close()
    elif arvo1 == "4":
        print("Lopetetaan.")
        tiedosto.close()
        break
    else:
        print("Tuntematon valinta.")
