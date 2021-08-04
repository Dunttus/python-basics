# -- coding: cp1252 --
import time

while True:
    print("(1) Read notes\n(2) Add an entry\n(3) Clear notebook\n(4)Quit\n")   
    value1 = input("What do you want to do?: ")
    file = open("memo.txt","r")
    contents = file.read()
    
    if value1 == "1":      
        print(contents)
    elif value1 == "2":
        file.close()
        number_value = input("Add new entry:")
        number_value = number_value + ":::" + time.strftime("%X %x") + "\n"
        file = open("memo.txt","a")
        kirjoita = file.write(number_value)
        file.close()
    elif value1 == "3":
        file.close()
        file = open("memo.txt","w")
        print("Notebook cleared.")
        file.close()
    elif value1 == "4":
        print("Quitting.")
        file.close()
        break
    else:
        print("Unknown selection.")