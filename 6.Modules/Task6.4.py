# -*- coding: cp1252 -*-

import inspector

while True:
    tested = input("Enter the word to test: ")
    results = inspector.testing(tested)
    if results == True:
        print("The word you entered is valid as a password!")
        break
    else:
        print("Invalid input.")