# -- coding: cp1252 --

luku = input("Anna luku: ")

try:
    luku = int(luku)
    print("Sy�te oli kelvollinen.")

except Exception:
    print("Virheellinen sy�te!")
