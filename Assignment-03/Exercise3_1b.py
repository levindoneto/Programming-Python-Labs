# Aufgabe 1 b

def exists (year, author): #exist >> existing book

    if year == None and author == None:
        return False
    else:
        if year == None:
            return author == 'Franz Kafka'
        if author == None:
            return year <=1645

    return year <=1645 and author == 'Franz Kafka'

      

print(exists(1543, None)) # should return True

print(exists(None, "Franz Kafka")) #should return True

print(exists(None, "Franz Beckenbauer")) #should return False

print(exists(None, None)) #should return False
