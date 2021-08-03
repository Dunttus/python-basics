# -- coding: cp1252 --

luku = input("Anna luku: ")

try:
    luku = int(luku)
    print("Syöte oli kelvollinen.")

except Exception:
    print("Virheellinen syöte!")
