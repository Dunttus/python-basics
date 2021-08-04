# -- coding: cp1252 --
value = input("Enter file name: ")
    
try:
    file = open(value, "r")
    contents = file.read()
    contents = int(contents)
    print("The result was obtained", contents + 313)
    
except FileNotFoundError:
    print("Invalid filename")
    
except Exception:
    print("Invalid file content, must be number!")