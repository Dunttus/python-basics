# -- coding: cp1252 --
import math

value1 = int(input("Enter first number: "))
value2 = int(input("Enter second number: "))

while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(value1/value2)\n(6)cos(value1/value2)\n(7)Change numbers\n(8)Quit")
    print("Selected figures:",value1,value2)
    selection = int(input("Choose a number (1-8): "))
    if selection == 1:
        print("Results is:", value1+value2)
    elif selection == 2:
        print("Results is:", value1-value2)
    elif selection == 3:
        print("Results is:", value1*value2)
    elif selection == 4:
        print("Results is:", value1/value2)
    elif selection == 5:
        print("Results is:",math.sin(value1/value2))
    elif selection == 6:
        print("Results is:",math.cos(value1/value2))
    elif selection == 7:
        value1 = int(input("Enter new first number: "))
        value2 = int(input("Enter new second number: "))
    elif selection == 8:
        break
    else:
        print("Selection not recognized.")