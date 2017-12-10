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