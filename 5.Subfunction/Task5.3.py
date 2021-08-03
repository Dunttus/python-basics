# -- coding: cp1252 --
def tulostaja(sana = "Oletustulostus"):
    print(sana)

def main():
    while True:
        syote = input("Anna syöte (Lopeta lopettaa): ")
        if syote == "Lopeta":
            break
        elif len(syote) < 5:
            tulostaja()
        else:
            tulostaja(syote)

if __name__ == "__main__":
    main()
