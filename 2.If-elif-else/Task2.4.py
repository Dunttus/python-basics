# -- coding: cp1252 --
arvo1 = input("Anna luku: ")
arvo2 = input("Anna toinen luku: ")
arvo1 = int(arvo1)
arvo2 = int(arvo2)

if arvo1%2 == 0 and arvo2%2 == 0:
    print("Molemmat luvut ovat parillisia.")
elif arvo1%2 != 0 and arvo2%2 != 0:
    print("Molemmat luvut ovat parittomia.")
else:
    print("Toinen luku on parillinen.")
