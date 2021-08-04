# -- coding: cp1252 --
file_name = input("Enter file name to be created: ")

file = open(file_name,"a")
file.close()

file_name2 = input("What is written to the file: ")

file = open(file_name,"w")
file.write(file_name2)
file.close()

print("File created",file_name, "and text writen in it:", file_name2)