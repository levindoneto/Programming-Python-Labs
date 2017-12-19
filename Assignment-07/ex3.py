''' EX3 - Assignment 07
    Amelie Fritsch, 3332267
    Vanessa Hindinger, 3324440
    Hana Kang, 3247297
    Levindo Gabriel Taschetto Neto, 3292080
'''

'''
    The solution for the problem of checking types of input can be seen specifically
    from the line 28 to the end, where the function type() and try except are used.
'''

l = [5,10,20,50,100,200,500] # Bills

l.sort(reverse=True)

# This is the dictionary in which we store the bills
storage = {}

while(True):
    ret = []
    userInput = input("Enter amount you want to withdraw or 'status':")
    #print("userInput: ", type(int(userInput)))

    if userInput == 'status':
        print(storage)
    else:
        try:
            amount = int(userInput)
            for d in l:
                ret.append(amount // d)
                amount = amount % d
            if amount > 0:
                print("The entered amount can not be withdrawn.")
            else:
                for d in reversed(range(len(l))):
                    if (ret[d] > 0):
                        print(str(l[d])+": "+str(ret[d]))
                        if l[d] in storage:
                            storage[l[d]] += ret[d]
                        else:
                            storage[l[d]] = ret[d]
        except ValueError:
            print("The only non-integer accept is 'status'!")
            continue
