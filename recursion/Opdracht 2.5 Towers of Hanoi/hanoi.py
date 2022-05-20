import pygame, time

"""
Recursive function to solve towers of Hanoi
"""
def towers_of_hanoi(n , source, destination, extra):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        game_loop(n, source, destination)
        return

    towers_of_hanoi(n-1, source, extra, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    game_loop(n, source, destination)
    towers_of_hanoi(n-1, extra, destination, source)



         
"""
Driver code
"""
n_disks = 3

# To be used when visualising
from visualise_hanoi import *
make_disks(n_disks)
update_visuals()
time.sleep(2)

towers_of_hanoi(n_disks,'A','C','B')
