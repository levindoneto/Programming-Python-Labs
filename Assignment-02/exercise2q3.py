import math

while (True):
	listBillsAmount = [[5, 0], [10, 0], [20, 0], [50, 0], [100, 0], [200, 0], [500, 0]]
	a = input("Enter amount you want to withdraw:\n")
	value = int (a)
	if (value%5!=0):
		print("Error")
	
	while (value >= 5):
		if (value>=500):
			listBillsAmount[6][1] = math.floor(value/500)
			value = value - 500*math.floor(value/500)
			
		elif (value<500 and value>=200):
			listBillsAmount[5][1] = math.floor(value/200)
			value = value - 200*math.floor(value/200)
		
		elif (value<200 and value>=100):
			listBillsAmount[4][1] = math.floor(value/100)
			value = value - 100*math.floor(value/100)
		
		elif (value<100 and value>=50):
			listBillsAmount[3][1] = math.floor(value/50)
			value = value - 50*math.floor(value/50)
		
		elif (value<50 and value>=20):
			listBillsAmount[2][1] = math.floor(value/20)
			value = value - 20*math.floor(value/20)
		
		elif (value<20 and value>=10):
			listBillsAmount[1][1] = math.floor(value/10)
			value = value - 10*math.floor(value/10)
		
		elif (value<10 and value>=5):
			listBillsAmount[0][1] = math.floor(value/5)
			value = value - 5*math.floor(value/5)
		else:
			print("error")
	
	for j in range(len(listBillsAmount)):
		if (listBillsAmount[j][1] != 0):
			print (listBillsAmount[j][0], ": ", listBillsAmount[j][1])
		
