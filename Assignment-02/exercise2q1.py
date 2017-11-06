firstName = "Nils" 
street = "Pfaffenwaldring"
house = "5b"
zip = 70569
city = "Stuttgart"
yearOfBirth = 1980
variablecurrentYear = 2017

ads = False # This variable controls whether the poor person will receive advertisement
'''
 The person gets advertisement if they are between 25 and 65 (ex-cluding) of age and live in zip codes below 10000 or above 60000 (including). We assume that there is a variablecurrentYear, set to 2017
'''

if (variablecurrentYear-yearOfBirth >= 25 and variablecurrentYear-yearOfBirth < 65 and (zip < 10000 or zip>=60000)):
	ads = True
else:
	ads = False

print ("ads: ", ads)