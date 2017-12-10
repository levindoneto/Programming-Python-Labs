#Exercise_4
#Question_3(a,b)

linewidth = 20
empty = "."
full = "#"

def emptyline():
    print(empty*linewidth)

def fromto(begin,end):
    s=""
    for i in range(0, begin):
        s = s + empty
    for i in range(begin, end):
        s = s + full
    for i in range(end, linewidth):
        s = s + empty
    print(s)

#Question 3(a):
def dots(pos1,pos2,pos3):
    y=""
    for j in range(0, pos1):
        y = y + empty
    for j in range(pos1, pos1+1):
        y = y + full
    for j in range(pos1+1,pos2):
        y = y + empty
    for j in range(pos2, pos2+1):
        y = y + full
    for j in range(pos2+1,pos3):
        y = y + empty
    for j in range(pos3, pos3+1):
        y = y + full
    for j in range (pos3+1,linewidth):
        y = y + empty
    print(y)
    
#Question 3(b):
def cross():  
    pos1=0
    pos2=linewidth-1
    for i in range (0, linewidth):
        s = ""
        for k in range(0, linewidth):
            if pos1==k or pos2==k:
                s = s + full
            else:
                s = s + empty
        print(s)
        pos1= pos1 + 1
        pos2= pos2 - 1


#verify:
dots(1,5,12)
print ("================================") 
cross()
            
    
