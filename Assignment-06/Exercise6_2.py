# this is the list of possible banknotes
l = [5,10,20,50,100,200,500]

# to make our lives easer, we sort them in DESCENDING order,
# i.e., the highest value is now first
l.sort(reverse=True)

sumOfbills = {}

# This program runs forever
while(True):
    # store number of returned bills
    ret = []
    amount = (input("Enter amount you want to withdraw: "))
    
    if amount == "status":
        for i in reversed(range(len(l))):
            try:
                print(str(l[i])+": "+str(sumOfbills[l[i]]))
            except KeyError:
                print(str(l[i])+": "+str(0))
    else:
        amount2 = int(amount)
        for d in l:
            ret.append(amount2 // d)
            amount2 = amount2 % d
        if amount2 > 0:
            print("The entered amount can not be withdrawn.")
        else:
            for d in reversed(range(len(l))):
                if (ret[d] > 0):
                    print(str(l[d])+": "+str(ret[d]))
                    sumOfbills[l[d]]= str(ret[d])

        
