
# a) b) c) d) e)

myDictionary = {
    'the': 'ART',
    'cat': 'NN',
    'meaows': 'VERB',
    'dog': 'NN',
    'cow': 'NN',
    'barks': 'VERB'}

#print(myDictionary.keys())
#print(myDictionary.values())
#print(myDictionary.items())

list = []
# b)
def tag (list):                                 
    list2=[]    # argument
    u = 0                                     
    for e in range(0,len(list)):
        if list[e] in myDictionary:
            list2.append(myDictionary[list[e]])
        else:                                       # c)
            u+=1
            list2.append('Other')
    print('Number of unknown words: '+str(u))       # d)        
    return(list2)

#e)
def tag2 (list):                                         
    list2=[]
    aDictionary = {'word': '', 'pos': ''}
    for e in range(0,len(list)):
        if list[e] in myDictionary:
            list2.append({'word': list[e], 'pos': myDictionary[list[e]]})
        else:
            list2.append({'word': list[e], 'pos': 'Other'})
    return(list2)
                 
    
