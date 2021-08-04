# -- coding: cp1252 --
tiedosto = open("passwords.txt","r")
sisalto = tiedosto.readlines()

for i in sisalto:
    i=i[:-1]
    if i.isalnum():
        print(i,"is valid as a password.")
    else:
        print(i,"contains invalid characters.")

        
tiedosto.close()