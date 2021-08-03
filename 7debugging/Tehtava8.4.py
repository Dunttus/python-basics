# -- coding: cp1252 --
import time
tiedosto = "muistio.txt"
while True:
    try:
        muistio = open(tiedosto,"r")
        muistio.close()
    except FileNotFoundError:
        print("Oletusmuistioa ei löydy, luodaan tiedosto.")
        muistio = open(tiedosto,"w")
        muistio.close()
        
    print("Käytetään muistiota: ",tiedosto)    
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Vaihda muistiota\n(5) Lopeta\n")   
    arvo1 = input("Mitä haluat tehdä?: ")
    muistio = open(tiedosto,"r")
    muistio.close()
    
    if arvo1 == "1":      
        muistio = open(tiedosto,"r")
        lista = muistio.read()
        print(lista)
        muistio.close()
    elif arvo1 == "2":
        muistio = open(tiedosto,"a")
        lukuarvo = input("Kirjoita uusi merkintä:")
        lukuarvo = lukuarvo + ":::" + time.strftime("%X %x") + "\n"
        kirjoita = muistio.write(lukuarvo)
        muistio.close()
    elif arvo1 == "3":
        muistio.close()
        muistio = open(tiedosto,"w")
        print("Muistio tyhjennetty.")
        muistio.close()
    elif arvo1 == "4":
        tiedosto2 = input("Anna tiedoston nimi: ")
        try:
            muistio = open(tiedosto2,"r")
            muistio.close()
            tiedosto = tiedosto2
        except FileNotFoundError:
            print("Tiedostoa ei löydy, luodaan tiedosto.")
            muistio = open(tiedosto2,"w")
            muistio.close()
            tiedosto = tiedosto2
    
    elif arvo1 == "5":
        print("Lopetetaan.")
        muistio.close()
        break
    else:
        print("Tuntematon valinta.")
