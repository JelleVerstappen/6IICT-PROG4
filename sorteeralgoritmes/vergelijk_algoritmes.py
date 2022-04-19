# Voeg matplotlib aan de sorteer_venv toe.
<<<<<<< HEAD
from typing import Counter
=======
>>>>>>> 8e4c1b1b3f9c9380b52e68a75a26a041a271c639
import matplotlib.pyplot as plt
import random
import algoritmes as a

def elementen_in_lijst(begin, eind):
    """
    Geef een lijst terug met alle waarden van begin 
    TEM eind.
<<<<<<< HEAD
    >>> elementen_in_lijst(1,4)
    [1,2,3,4]
    """
    lijst = []
    for n in range(begin, eind+1):
        lijst.append(n)
    return lijst
=======

    >>> elementen_in_lijst(1,4)
    [1,2,3,4]
    
    """
>>>>>>> 8e4c1b1b3f9c9380b52e68a75a26a041a271c639

def genereer_unieke_lijst(n):
    """
    Gegeven een aantal elementen. Genereer een willekeurige lijst,
    met enkel unieke waarden. De maximale waarde mag niet groter zijn
    dan het (aantal elementen-1).
<<<<<<< HEAD
    >>> genereer_unieke_lijst(6):
    [1,4,3,2,5,0]
    """
    rand_lijst = random.sample(range(0, n), n)

    return rand_lijst
=======

    >>> genereer_unieke_lijst(6):
    [1,4,3,2,5,0]
    
    """
>>>>>>> 8e4c1b1b3f9c9380b52e68a75a26a041a271c639

def iteraties_algoritme(unieke_lijst, algoritme):
    """
    Gegeven een willekeurige lijst, met enkel unieke waarden en het algoritme. 
    Geef het aantal keer terug dat de generator uit de functie
    "geyield" is om deze lijst te sorteren.
<<<<<<< HEAD
    >>> iteraties_algoritme([0 ,8, 3, 2, 5], algoritme)
    22
    """
    actief_algoritme_generator = algoritme(unieke_lijst)
    counter = 0
    while True:
            try:
                next(actief_algoritme_generator)
                counter += 1
            except StopIteration: # Als de lijst helemaal doorlopen geeft de generator deze error
                sorteren = False
                return counter
=======

    >>> iteraties_algoritme([0 ,8, 3, 2, 5], algoritme)
    22

    """
>>>>>>> 8e4c1b1b3f9c9380b52e68a75a26a041a271c639
    
def overloop_iteraties(lijst, algoritme):
    """
    Gegeven een lijst van oplopende integers, die het aantal te sorteren
    elementen voorstellen, en een bepaald algoritme. 
    Voer voor iedere integer iteraties_algoritme() uit. 
    Geef een lijst terug met iedere waarde die iteraties_algoritme() teruggaf.
<<<<<<< HEAD
    >>> overloop_iteraties([2,3,4,5], algoritme)
    [5,8,15,27]
    """
    result = []
    for i in lijst:
        iteraties = iteraties_algoritme(genereer_unieke_lijst(i), algoritme)
        result.append(iteraties)
    return result
=======

    >>> overloop_iteraties([2,3,4,5], algoritme)
    [5,8,15,27]
    
    """
>>>>>>> 8e4c1b1b3f9c9380b52e68a75a26a041a271c639

def main():
    
    # Begin en eind waarde aantal te sorteren elementen
    begin = 2
<<<<<<< HEAD
    eind = 40
=======
    eind = 100
>>>>>>> 8e4c1b1b3f9c9380b52e68a75a26a041a271c639
    
    lijst_aantal_blokken = elementen_in_lijst(begin, eind)

    # Bozo enkel gebruiken zolang aantal te sorteren elementen <9 is.
    bozo_aan = False

    # Overloop de verschillende algoritmes
    iteraties_bubbel = overloop_iteraties(lijst_aantal_blokken, a.bubbel_sort)
    iteraties_insertion = overloop_iteraties(lijst_aantal_blokken, a.insertion_sort)
<<<<<<< HEAD
     #iteraties_merge = overloop_iteraties(lijst_aantal_blokken, a.merge_sort)
=======
    iteraties_merge = overloop_iteraties(lijst_aantal_blokken, a.merge_sort)
>>>>>>> 8e4c1b1b3f9c9380b52e68a75a26a041a271c639
    iteraties_bozo = []
    if bozo_aan:
        iteraties_bozo = overloop_iteraties(lijst_aantal_blokken, a.bozo_sort)

    # Plot de verschillende algoritmes samen met het aantal te sorteren blokken.
    plt.plot(lijst_aantal_blokken, iteraties_bubbel)
    plt.plot(lijst_aantal_blokken, iteraties_insertion)
<<<<<<< HEAD
    #plt.plot(lijst_aantal_blokken, iteraties_merge)
=======
    plt.plot(lijst_aantal_blokken, iteraties_merge)
>>>>>>> 8e4c1b1b3f9c9380b52e68a75a26a041a271c639
    if bozo_aan:
        plt.plot(lijst_aantal_blokken, iteraties_bozo)
    
    # Voeg opmaak toe.
    plt.title("Vergelijking performance sorteeralgoritmes")
    plt.ylabel("Iteraties ~ Processing Power")
    plt.xlabel("Elementen")
    plt.legend(["Bubbel","Insertion","Merge","Bozo"])

    plt.show()
            
    

# Zorgt ervoor dat de main functie uitgevoerd wordt, maar enkel indien het bestand sorteer_algoritme.py uitgevoerd wordt.
if __name__ == "__main__":
    main()