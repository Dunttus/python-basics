# -- coding: cp1252 --
def tulostaja(sana):
    print ("Antamasi sy�te oli",len(sana),"merkki� pitk�.") 

def main():
    while True:
        syote = input("Anna sy�te (Lopeta lopettaa): ")
        if syote == "Lopeta":
            break
        elif syote == "":
            print("Et antanut sy�tett�")
        else:
            tulostaja(syote)

if __name__ == "__main__":
    main()
