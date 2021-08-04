# -- coding: cp1252 --
value1 = input("Enter the first number: ")
value2 = input("Enter the second number: ")
value1 = int(value1)
value2 = int(value2)

if value1%2 == 0 and value2%2 == 0:
    print("Both numbers are even.")
elif value1%2 != 0 and value2%2 != 0:
    print("Both numbers are odd.")
else:
    print("The second number is even.")