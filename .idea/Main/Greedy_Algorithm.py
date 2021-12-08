from Package_Data import *
from Distance_Data import *


def greedy_algorithm(my_hash, truck):
    print('working on it')
    for i in range(1, 40):
        while(float(my_hash.search(i).distance) < 5) and (len(truck.table) < 17):
            truck.insert(my_hash.search(i).ID)
    return truck