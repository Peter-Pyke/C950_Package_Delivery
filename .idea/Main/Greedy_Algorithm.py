from Package_Data import *
from Distance_Data import *


def greedy_algorithm(my_hash, truck):
    """
    loop through my hash table to find the package with the shortest distance, earliest delivery
    time and status at hub. Once that package is found check note and adjust as needed. Right before
    appending the package to the truck list change its status to en route.

    for the second package use the address of the first package and find the package closest to that
    address with the earliest delivery time and status at hub. continue this until truck has 16 packages.

    for delivery add the distance of each delivery and return trip to hub if needed to the truck distance
    traveled.

    Figure out how to calculate time based off of distance traveled assuming you start at 8am.

    :param my_hash:
    :param truck:
    :return:
    """