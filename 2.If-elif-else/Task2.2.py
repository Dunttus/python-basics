# -- coding: cp1252 --
name1 = input("Enter name: ")

if name1 == "Joni":
	secret_value1 = input("Enter password: ")
	
	if secret_value1 == "password":
		print("The password and name correct!")
	else:
		print("Password incorrect.")
else:
	print("Name incorrect.")