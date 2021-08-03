def testaa(lause):
    if len(lause) <= 4:
        return False
    elif lause.isalpha() == True:
        return False
    elif lause.isdigit() == True:
        return False
    else:
        return True
