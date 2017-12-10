#Exercise 4

#Aufgabe 2

#Define the list of possible bills
l = [5, 10, 20, 50, 100, 200, 500]

#Ask customer for Whitdrawal input
print('Please insert, how much money you need')
a = input()
b = int(a)

#Program for an ATM that hands out perfectly fitting amount of bills
#ret means return
ret_500 = b // 500
b = b % 500

ret_200 = b // 200
b = b % 200

ret_100 = b // 100
b = b % 100

ret_50 = b // 50
b = b % 50

ret_20 = b // 20
b = b % 20

ret_10 = b // 10
b = b % 10

ret_5 = b // 5
b = b % 5


#Start the programm
while(b > 0):
    b
if b < 0:
    print('Please insert a guilty number.')
else:
    if ret_5 > 0:
        print('5: ' + str(ret_5))
    if ret_10 > 0:
        print('10: ' + str(ret_10))
    if ret_20 > 0:
        print('20: ' + str(ret_10))
    if ret_50 > 0:
        print('50: ' + str(ret_50))
    if ret_100 > 0:
        print('100: ' + str(ret_100))
    if ret_200 > 0:
        print('200: ' + str(ret_200))
    if ret_500 > 0:
        print('500: ' + str(ret_500))
        

    
