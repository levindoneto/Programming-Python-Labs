def exists(pubYear, author):
    if pubYear=='Franz Kafka' or pubYear<1645 and author=='Franz Kafka' or author== None:
        return True
    else:
        return False
    if pubYear==None and author<1645 or author=='Franz Kafka':
        return True
    else:
        return False

try:
    print(exists(1643,'Franz Kafka')) #true
    print(exists(1684, 'Hana'))   #false
    print(exists(1644, None))     #true
    print(exists('Franz Kafka',1643)) #true
    print(exists(None, None))     #false
    
except TypeError:
    print('False')



