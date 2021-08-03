# -- coding: cp1252 --
lukuarvo = input("Minkäniminen tiedosto luodaan?:")

tiedosto = open(lukuarvo,"a")
tiedosto.close()

lukuarvo2 = input("Mitä kirjoitetaan tiedostoon?:")

tiedosto = open(lukuarvo,"w")
tiedosto.write(lukuarvo2)
tiedosto.close()

print("Luotiin tiedosto",lukuarvo, "ja siihen tallennettiin teksti:", lukuarvo2)
