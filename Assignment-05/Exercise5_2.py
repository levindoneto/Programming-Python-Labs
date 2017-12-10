#Exercise5_2


#(a)This function adds two numbers.
def f(x, y):
    return(x+y)

#(b)This function adds all the numbers, except y,in the sequence, which started with x and ended with y.
def f(x,y):
    a = 0
    for i in range(x,y):
        a +=1
    retrun(a)

#(c)This function gets only number "0" as the result no matter which arguments we give to x and y.
def f(x,y):
    r = 0
    for i in range(0,x):
        r = r*x
    return(r)

#(d)This function verifies if a number can be divided by 2.
def f(x):
    return (x%2 == 0)

#(e)This function verifies if number x >= number y and number x <= number z.
def f(x,y,z):
    return(x >= y & x <= z)

#(f)This function makes a number always a real number.
def f(x):
    if x < 0:
        return(-1*x)
    else:
        return(x)

#(g)This function....
def f(x,y):
    z = 0
    for e in x:
        if e==y:
            z +=1
    return(z)
