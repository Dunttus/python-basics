def testing(sentence):
    if len(sentence) <= 4:
        return False
    elif sentence.isalpha() == True:
        return False
    elif sentence.isdigit() == True:
        return False
    else:
        return True