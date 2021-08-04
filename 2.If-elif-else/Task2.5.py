value1 = input("Enter first number: ")
value2 = input("Enter second number: ")
value1 = int(value1)
value2 = int(value2)

print("""(1) +
(2) -
(3) *
(4) /""")
value3 = input("Select a number (1-4): ")

if value3 == "1":
    print("Result is: ",value1+value2)
elif value3 == "2":
    print("Result is: ",value1-value2)
elif value3 == "3":
    print("Result is: ",value1*value2)
elif value3 == "4":
    print("Result is: ",value1/value2)
else:
    print("Selection not recognized.")