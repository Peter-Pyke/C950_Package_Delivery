from Package_Data import *
from Distance_Data import *
from datetime import datetime



def load_truck_1(my_hash, truck):
    for i in range(1, 41):
        package = my_hash.search(i)
        package_id = package.ID
        delivery_time = package.deadline
        no_delay = package.no_delay
        truck_number = package.truck
        EOD = datetime.strptime('08:00 PM', "%I:%M %p")

        if (truck_number == 1) and (len(truck.table) < 16) and package.status == 'AT HUB':
            package.status = 'EN ROUTE'
            truck.insert(package_id)

    for i in range(1, 41):
        package = my_hash.search(i)
        package_id = package.ID
        delivery_time = package.deadline
        no_delay = package.no_delay
        truck_number = package.truck
        EOD = datetime.strptime('08:00 PM', "%I:%M %p")

        if (delivery_time < EOD) and (no_delay) and (len(truck.table) < 16):
            package.status = 'EN ROUTE'
            truck.insert(package_id)
        elif (truck_number == None) and (len(truck.table) < 16):
            package.status = 'EN ROUTE'
            truck.insert(package_id)

def load_truck_2(my_hash, truck):
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
    for i in range(1, 41):
        package = my_hash.search(i)
        package_id = package.ID
        delivery_time = package.deadline
        no_delay = package.no_delay
        truck_number = package.truck
        EOD = datetime.strptime('08:00 PM', "%I:%M %p")

        if(package.status == 'AT HUB') and (len(truck.table) < 16):
            package.status = 'EN ROUTE'
            truck.insert(package_id)
