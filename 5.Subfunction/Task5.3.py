# -- coding: cp1252 --
def printer(word = "Word must be more than 4 letters"):
    print(word)

def main():
    while True:
        user_input = input("Type quit to stop \nEnter word: ")
        if user_input == "quit":
            break
        elif len(user_input) < 5:
            printer()
        else:
            printer(user_input)

if __name__ == "__main__":
    main()