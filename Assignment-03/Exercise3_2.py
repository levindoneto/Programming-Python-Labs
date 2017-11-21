units = 100

def balance():
    return units
def withdraw(given,units):
    
    try:
       return units -int(given)
        
    except ValueError:
        print('Not a number')
    
def interest():
    return int(units*1.10)
def project(rate):
    print(int((units*(1+rate)**10)))

print(balance()) # prints 100
units = withdraw(10,units)
print(balance()) # prints 90
withdraw("ten",units)  # prints "Not a number"
units = interest()
print(balance()) # prints 99.0
units = withdraw(9,units)
print(balance()) # prints 90.0
units = withdraw(-20,units)
print(balance()) # prints 110.0
project(0.2)# prints 567.5758
print(balance()) # prints 110.0
           
