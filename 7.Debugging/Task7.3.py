# -- coding: cp1252 --
import math

def number_Inspector():
    while True:
        try:
            value = int(input("Enter value: "))
            return value
        except Exception:
            print("Invalid input!")

def main():
    value1 = number_Inspector()
    value2 = number_Inspector()
    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(value1/value2)\n(6)cos(value1/value2)\n(7)Change the numbers\n(8)Quit")
        print("Selected figures:",value1,value2)
        valinta = int(input("Make a choice (1-8): "))
        if valinta == 1:
            print("The result is:", value1+value2)
        elif valinta == 2:
            print("The result is:", value1-value2)
        elif valinta == 3:
            print("The result is:", value1*value2)
        elif valinta == 4:
            print("The result is:", value1/value2)
        elif valinta == 5:
            print("The result is:",math.sin(value1/value2))
        elif valinta == 6:
            print("The result is:",math.cos(value1/value2))
        elif valinta == 7:
            value1 = number_Inspector()
            value2 = number_Inspector()
        elif valinta == 8:
            break
        else:
            print("Selection not recognized.")
            
if __name__ == "__main__":
    main()