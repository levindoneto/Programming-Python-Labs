''' EX2(a) - Assignment 07 
    Amelie Fritsch, 3332267
    Vanessa Hindinger, 3324440
    Hana Kang, 3247297
    Levindo Gabriel Taschetto Neto, 3292080
'''

import re

''' Function that recognizes spaces as tokens '''
def tokenize1(strInput):
	splitList = []
	for p in re.split("[ ]",strInput):
		if (p != None):
			splitList.append(p) # Add a piece of the string into the list of pieces

	return splitList

''' Tests '''
print(tokenize1('hello world'))
print(tokenize1('hello! world!'))
print(tokenize1('Mr. Anderson.'))
