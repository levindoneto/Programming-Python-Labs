''' EX2(b) - Assignment 07 
    Amelie Fritsch, 3332267
    Vanessa Hindinger, 3324440
    Hana Kang, 3247297
    Levindo Gabriel Taschetto Neto, 3292080
'''

import re

''' Function that recognizes full stops, commas, exclamation and question marks, and spaces as tokens '''
def tokenize2(strInput):
	re.split(r'(!|\s)\s*', strInput)
	return re.split(r'(!|.\s)\s*', strInput) # \s: separate by space
