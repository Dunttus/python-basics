# -*- coding: cp1252 -*-
import random

draws = 0
loses = 0
wins = 0
round = 0


while True:
    number_value = input("Stone, Paper vai Scissors? (quit ends):")

    if number_value == "Stone":
        value = random.randint(1,3)
        print("You chose:", number_value)
        if value == 1:
            print("Computer chose: Stone")
            print("Draw!")
            round += 1
            draws += 1
        elif value == 2:
            print("Computer chose: Paper")
            print("You lost!")
            round += 1
            loses += 1
        else:
            print("Computer chose: Scissors")
            print("You won!")
            round += 1
            wins += 1
            
    elif number_value == "Paper":
        value = random.randint(1,3)
        print("You chose:", number_value)
        if value == 1:
            print("Computer chose: Stone")
            print("You won!")
            round += 1
            wins += 1
        elif value == 2:
            print("Computer chose: Paper")
            print("Draw!")
            round += 1
            draws += 1
        else:
            print("Computer chose: Scissors")
            print("You lost!")
            round += 1
            loses += 1
            
    elif number_value == "Scissors":
        value = random.randint(1,3)
        print("You chose:", number_value)
        if value == 1:
            print("Computer chose: Stone")
            print("You lost!")
            round += 1
            loses += 1
        elif value == 2:
            print("Computer chose: Paper")
            print("You won!")
            round += 1
            wins += 1
        else:
            print("Computer chose: Scissors")
            print("Draw!")
            round += 1
            draws += 1
            
    elif number_value == "quit":
        print("Played",round,"rounds of which You won",wins,"and you played evenly",draws,"times.")
        break
    else:
        print("")