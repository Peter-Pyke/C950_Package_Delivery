from Trucks import Truck
from datetime import datetime, timedelta
from My_Hash_Table import ChainingHashTable
from Distance_Data import loadDistanceData, distanceLookUp



def deliver_packages(myHash, distance_data, look_up_dictionary, Truck):

    # Repeats the code below until the truck is empty
    while (len(Truck.table)>0):

        # Holds the distance of the first index package
        shortest_distance = float(myHash.search(Truck.table[0]).distance)

        # Loops through all packages on the truck and saves the one with the shortest delivery distance
        for i in range(len(Truck.table)):
            if float(myHash.search(Truck.table[i]).distance) <= shortest_distance:
                shortest_distance = float(myHash.search(Truck.table[i]).distance)
                packageID = Truck.table[i]

        # Updates the distance for each package based off the current location
        for i in range(len(Truck.table)):
            distance_to_delivery_address = distance_data[look_up_dictionary[myHash.search(packageID).address]][look_up_dictionary[myHash.search(Truck.table[i]).address]]
            myHash.search(Truck.table[i]).distance = distance_to_delivery_address

        # Distance truck traveled to deliver the current package
        distance_to_add = float(distance_data[look_up_dictionary[Truck.current_location]][look_up_dictionary[myHash.search(packageID).address]])

        # Updates truck current time base off of  miles traveled
        Truck_time = Truck.current_time
        minutes_to_add = (distance_to_add*3.33)
        current_time = Truck_time + timedelta(minutes=minutes_to_add)
        Truck.current_time = current_time

        # Updates the status of the package
        myHash.search(packageID).time_delivered = current_time
        myHash.search(packageID).status = 'DELIVERED'

        # Updates the Truck location, total distance and removes delivered packages
        Truck.update_distance(distance_to_add)
        Truck.update_location(myHash.search(packageID).address)
        Truck.table.remove(packageID)

    # Returns truck to hub, adds distance and time to get back
    distance_back = float(distance_data[look_up_dictionary[Truck.current_location]][look_up_dictionary['4001 South 700 East']])
    Truck.update_distance(distance_back)
    Truck.current_time = Truck.current_time + timedelta(minutes=(distance_back*3.33))
    Truck.update_location('4001 South 700 East')





