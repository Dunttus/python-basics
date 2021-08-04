# -- coding: cp1252 --
def printer(word):
    print ("Input was",len(word),"characters long.") 

def main():
    while True:
        user_input = input("Write quit to stop \nEnter word: ")
        if user_input == "quit":
            break
        elif user_input == "":
            print("Input was not given")
        else:
            printer(user_input)

if __name__ == "__main__":
    main()