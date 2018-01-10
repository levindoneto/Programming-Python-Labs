''' Exercise 8__Aufgabe 1
    Amelie Fritsch, 3332267
    Vanessa Hindinger, 3324440
    Hana Kang, 3247297
    Levindo Gabriel Taschetto Neto, 3292080
'''

''' write a function called isZipCode(inputString) that takes a string
    as an argument and returns a boolean value. The value is true if the
    inputString is a German zip code. Germen zip codes are always five
    digits long and all digits are allowed.
'''

def isZipCode(inputString):
    if len(inputString) !=5:
        return False
    for i in range(0,5):
        if not inputString[i].isdecimal():
            return False
    return True

print(isZipCode("10093"))

    
    
