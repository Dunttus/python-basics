# -- coding: cp1252 --
import math
def lukuTarkastaja():
    while True:
        try:
            luku = int(input("Anna luku: "))
            return luku
        except Exception:
            print("Virheellinen syöte!")

def main():
    luku1 = lukuTarkastaja()
    luku2 = lukuTarkastaja()
    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(luku1/luku2)\n(6)cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta")
        print("Valitut luvut:",luku1,luku2)
        valinta = int(input("Tee valinta (1-8): "))
        if valinta == 1:
            print("Tulos on:", luku1+luku2)
        elif valinta == 2:
            print("Tulos on:", luku1-luku2)
        elif valinta == 3:
            print("Tulos on:", luku1*luku2)
        elif valinta == 4:
            print("Tulos on:", luku1/luku2)
        elif valinta == 5:
            print("Tulos on:",math.sin(luku1/luku2))
        elif valinta == 6:
            print("Tulos on:",math.cos(luku1/luku2))
        elif valinta == 7:
            luku1 = lukuTarkastaja()
            luku2 = lukuTarkastaja()
        elif valinta == 8:
            break
        else:
            print("Valintaa ei tunnistettu.")
            
if __name__ == "__main__":
    main()
