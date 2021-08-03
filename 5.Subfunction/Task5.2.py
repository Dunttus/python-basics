# -- coding: cp1252 --
def toinenpotenssi(luku1):
    lasku = luku1**2
    return lasku

def main():
    luku1 = int(input("Anna lukuarvo: "))
    print("Toinen potenssi on ", toinenpotenssi(luku1))

if __name__ == "__main__":
    main()
