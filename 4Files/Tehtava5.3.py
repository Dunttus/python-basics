# -- coding: cp1252 --
tiedosto = open("merkkijonoja.txt","r")
sisalto = tiedosto.readlines()

for i in sisalto:
    i=i[:-1]
    if i.isalnum():
        print(i,"kelpaa salasanaksi.")
    else:
        print(i,"sisältää virheellisiä merkkejä.")

        
tiedosto.close()
