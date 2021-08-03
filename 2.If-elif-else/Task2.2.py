# -- coding: cp1252 --
nimi1 = input("Anna nimi: ")

if nimi1 == "Erkki":
	salasana1 = input("Anna salasana: ")
	
	if salasana1 == "Esimerkki":
		print("Salasana ja nimi oli oikein!")
	else:
		print("Salasana oli väärin.")
else:
	print("Nimi oli väärin.")
