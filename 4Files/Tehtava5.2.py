# -- coding: cp1252 --
lukuarvo = input("Mink�niminen tiedosto luodaan?:")

tiedosto = open(lukuarvo,"a")
tiedosto.close()

lukuarvo2 = input("Mit� kirjoitetaan tiedostoon?:")

tiedosto = open(lukuarvo,"w")
tiedosto.write(lukuarvo2)
tiedosto.close()

print("Luotiin tiedosto",lukuarvo, "ja siihen tallennettiin teksti:", lukuarvo2)
