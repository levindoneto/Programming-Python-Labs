''' Exercise 8__Aufgabe 1
    Amelie Fritsch, 3332267
    Vanessa Hindinger, 3324440
    Hana Kang, 3247297
    Levindo Gabriel Taschetto Neto, 3292080
'''

''' Write a function called isPhoneNumber(inputString),
that takes a string as an argument and returns a boolean
value. The boolean value is true, if and only if the
inputString represents a domestic phone number. Domestic
phone numbers consist of an area code and a local number.
Both are separated by a space or minus sign. The area code
starts with a zero and is between three and five digits long.
The local number is between 4 and 10 digits long, and never
starts with a zero.
'''

def isPhoneNumber(inputString):
    if len(inputString) !=13:
        return False
    if inputString[0]!= "0":
        return False
    for i in range(1,4):
        if not inputString[i].isdecimal():
            return False
    if inputString[4]!= " " and inputString[4]!= "-":
        return False
    for i in range(5,13):
        if not inputString[i].isdecimal():
            return False
    if inputString[5]== "0":
        return False
    return True

print(isPhoneNumber("0711 91218792"))


    
