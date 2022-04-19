import random

# Vooraleer het algoritme hier te implementeren. Probeer het eerst met een kleine lijst in test.py

# Het bubbel_sort algoritme, deze is gegeven ter verduidelijking van de werking van generatoren
def bubbel_sort(lijst):
    for i in range(len(lijst)-1): #We kijken naar huidig en volgend blok
        for j in range(len(lijst)-1-i):
            waarde1 = lijst[j]
            waarde2 = lijst[j+1]

            if (waarde1 > waarde2):
               #lijst[j], lijst[j+1] = lijst[j+1], lijst[j] #Snellere methode om onderstaande te bereiken
               tmp = lijst[j]
               lijst[j]=lijst[j+1]
               lijst[j+1]=tmp

            yield j, j+1 # Volgorde: Groen blok (links), Rood blok (rechts)

# Het insertion_sort algoritme
def insertion_sort(lijst):
    for index in range(1, len(lijst)):
        currentValue = lijst[index]
        currentPosition = index

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        while currentPosition > 0 and lijst[currentPosition - 1] > currentValue:
            lijst[currentPosition] = lijst[currentPosition -1]
            currentPosition = currentPosition - 1

            j = currentPosition

            yield j, j-1
        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        lijst[currentPosition] = currentValue


# Het bozo_sort algoritme. 
def bozo_sort(lijst):
    # Gebruik als yield -2. Alle blokken worden tegelijk gewisseld. Een actief blok aanduiden is dus niet mogelijk
    shuffled = random.shuffle(lijst)
    while shuffled != sorted(lijst):
        shuffled = random.shuffle(lijst)

        yield -2, -2








        
        

