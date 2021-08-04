# -- coding: cp1252 --

value = input("Enter number: ")

try:
    value = int(value)
    print("The input was valid.")

except Exception:
    print("Invalid input!")