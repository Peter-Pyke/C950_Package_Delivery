from Package_Data import *
from Distance_Data import *
from datetime import datetime
from Package_Data import Package


# This checks to see if any packages with delivery times less then EOD and without delays are still at hub.
def check_delivery_times_no_delay(myHash):
    EOD = datetime.strptime('08:00 PM', "%I:%M %p")
    for i in range(1, 41):
        deliver_by_time = myHash.search(i).deadline
        if deliver_by_time < EOD and myHash.search(i).status == 'AT HUB' and myHash.search(i).no_delay:
            return False
    return True
# This checks to see if any packages with delivery times less then EOD still at hub (package can have delay).
def check_delivery_times_delay_included(myHash):
    EOD = datetime.strptime('08:00 PM', "%I:%M %p")
    for i in range(1, 41):
        deliver_by_time = myHash.search(i).deadline
        if deliver_by_time < EOD and myHash.search(i).status == 'AT HUB':
            return False
    return True
# This checks to see if any packages with delivery times less then EOD still at hub (package can have delay).
def check_hub_for_packages(myHash):
    for i in range(1, 41):
        if myHash.search(i).status == 'AT HUB':
            return True
    return False
def load_truck_1(my_hash, truck):

    while(len(truck.table) < 16 and check_hub_for_packages(my_hash)):

        for i in range(1, 41):
            count = len(truck.table)
            package = my_hash.search(i)
            package_id = package.ID
            delivery_time = package.deadline
            no_delay = package.no_delay
            truck_number = package.truck
            EOD = datetime.strptime('08:00 PM', "%I:%M %p")

            if ((truck_number == 1) and (len(truck.table) < 16) and (package.status == 'AT HUB')):
                package.status = 'EN ROUTE'
                truck.insert(package_id)
            elif (delivery_time < EOD ) and (no_delay) and (len(truck.table) < 16) and (truck_number != 2) and (package.status == 'AT HUB'):
                package.status = 'EN ROUTE'
                truck.insert(package_id)
            elif check_delivery_times_no_delay(my_hash) and (package.status == 'AT HUB') and (len(truck.table) < 16):
                package.status = 'EN ROUTE'
                truck.insert(package_id)



def load_truck_2(my_hash, truck):
    while(len(truck.table) < 16 and check_hub_for_packages(my_hash)):
        for i in range(1, 41):
            package = my_hash.search(i)
            package_id = package.ID
            delivery_time = package.deadline
            no_delay = package.no_delay
            truck_number = package.truck
            EOD = datetime.strptime('08:00 PM', "%I:%M %p")

            if(package.status == 'AT HUB') and (delivery_time < EOD) and (len(truck.table) < 16):
                package.status = 'EN ROUTE'
                truck.insert(package_id)
            elif check_delivery_times_delay_included(my_hash) and package.status == 'AT HUB' and (len(truck.table) < 16):
                package.status = 'EN ROUTE'
                truck.insert(package_id)


