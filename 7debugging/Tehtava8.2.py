# -- coding: cp1252 --
luku = input("Anna tiedoston nimi: ")
    
try:
    tiedosto = open(luku, "r")
    sisalto = tiedosto.read()
    sisalto = int(sisalto)
    print("Saatiin tulos", sisalto + 313)
    
except FileNotFoundError:
    print("Virheellinen tiedostonnimi")
    
except Exception:
    print("Tiedoston sisältö virheellinen!")
