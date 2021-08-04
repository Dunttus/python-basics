# -- coding: cp1252 --
file = open("memo.txt","r")
contents = file.read()

print("Text was read from file: ",contents)

file.close()