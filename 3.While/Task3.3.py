# -- coding: cp1252 --
value1 = int(input("How many rounds?: "))
round = 0
counter = 0

for round in range(value1):

    counter = counter + round
    round = round + 1
    
print("Accumulation was obtained:", counter)