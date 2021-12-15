from Package_Data import *
from Distance_Data import *
from datetime import datetime
from Package_Data import Package



# This checks to see if any packages with delivery times less then EOD still at hub (package can have delay).
def check_hub_for_packages(myHash):
    for i in range(1, 41):
        if myHash.search(i).status == 'AT HUB':
            return True
    return False
# Loads the trucks with the packages in a predefined order
def load_truck(my_hash, truck):
#    packages_to_load = [15,	1,	13,	19,	14,	16,	20,	29,	30,	31,	34,	37,	40,	2,	4,	21,	18,	36,	38,	3,	6, 28,	32,	25,
#                        5,	7,	8,	9,	10,	11,	12,	17,	22,	23,	24,	26,	27,	33,	35,	39]
    packages_to_load = [15,	1,	13,	19,	14,	16,	20,	29,	30,	31,	34,	37,	40,	2,	4,	21,	18,	36,	38,	3,	6, 28,	32,	25,
                        5,	7,	8, 39,	10,	11,	12,	17,	22,	23,	24,	26,	27,	33,	35,	9]
    while(len(truck.table) < 16 and check_hub_for_packages(my_hash)):
        for i in packages_to_load:
            package = my_hash.search(i)
            package_id = package.ID

            if(package.status == 'AT HUB') and len(truck.table) < 16:
                package.time_loaded_on_truck = truck.current_time
                package.status = 'EN ROUTE'
                truck.insert(package_id)
