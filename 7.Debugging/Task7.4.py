# -- coding: cp1252 --
import time
file = "memo.txt"
while True:
    try:
        memo = open(file,"r")
        memo.close()
    except FileNotFoundError:
        print("Default file not found, creating new text file.")
        memo = open(file,"w")
        memo.close()
        
    print("Using notebook: ",file)    
    print("(1) Read notes\n(2) Add an entry\n(3) Clear notebook\n(4) Change notebook\n(5) Quit\n")   
    arvo1 = input("What you want to do?: ")
    memo = open(file,"r")
    memo.close()
    
    if arvo1 == "1":      
        memo = open(file,"r")
        lista = memo.read()
        print(lista)
        memo.close()
    elif arvo1 == "2":
        memo = open(file,"a")
        number_value = input("Write a new entry:")
        number_value = number_value + ":::" + time.strftime("%X %x") + "\n"
        kirjoita = memo.write(number_value)
        memo.close()
    elif arvo1 == "3":
        memo.close()
        memo = open(file,"w")
        print(file, "cleared")
        memo.close()
    elif arvo1 == "4":
        file2 = input("Enter a file name: ")
        try:
            memo = open(file2,"r")
            memo.close()
            file = file2
        except FileNotFoundError:
            print("File not found, creating file.")
            memo = open(file2,"w")
            memo.close()
            file = file2
    
    elif arvo1 == "5":
        print("Quitting.")
        memo.close()
        break
    else:
        print("Unknown selection.")
