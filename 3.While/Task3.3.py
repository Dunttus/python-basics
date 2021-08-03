# -- coding: cp1252 --
arvo1 = int(input("Kuinka monta kierrosta?:"))
kierros = 0
laskuri = 0

for kierros in range(arvo1):

    laskuri = laskuri + kierros
    kierros = kierros + 1
    
print("Kertymäksi saatiin:", laskuri)
    
