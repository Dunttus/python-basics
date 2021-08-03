# -- coding: cp1252 --
def tulostaja(sana):
    print ("Antamasi syöte oli",len(sana),"merkkiä pitkä.") 

def main():
    while True:
        syote = input("Anna syöte (Lopeta lopettaa): ")
        if syote == "Lopeta":
            break
        elif syote == "":
            print("Et antanut syötettä")
        else:
            tulostaja(syote)

if __name__ == "__main__":
    main()
