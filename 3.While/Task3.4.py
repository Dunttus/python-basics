# -- coding: cp1252 --
continuation = True
number = 0

while continuation:
    if number ==0:
        value1 = int(input("Enter first number: "))
        value2 = int(input("Enter second number: "))
        number +=1
    elif number >= 1:
        value1 = int(input("Enter new first number: "))
        value2 = int(input("Enter new second number: "))
    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change the numbers\n(6)Quit")
        print("Valitut luvut:", value1, value2)
        value3 = input("Select number (1-6): ")
        if value3 == "1":
            print("Result is: ",value1+value2)
        elif value3 == "2":
            print("Result is: ",value1-value2)
        elif value3 == "3":
            print("Result is: ",value1*value2)
        elif value3 == "4":
            print("Result is: ",value1/value2)
        elif value3 == "5":
            break
        elif value3 == "6":
            continuation = False
            break
        else:
            print("Selection not recognized.")