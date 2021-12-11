from Trucks import Truck
from datetime import datetime
from My_Hash_Table import ChainingHashTable
from Distance_Data import loadDistanceData, distanceLookUp



def deliver_packages(myHash, distance_data, look_up_dictionary, Truck):

    """
    count = 0
    for i in range(len(Truck.table)):
        count += 1

        if (myHash.search(Truck.table[i]).distance <= myHash.search(Truck.table[i-1]).distance):
            packageID_to_deliver = Truck.table[i]

        if (count == len(Truck.table)):
            distance_to_add = float(distance_data[look_up_dictionary[Truck.current_location]][look_up_dictionary[myHash.search(packageID_to_deliver).address]])
            print(distance_to_add)
            myHash.search(packageID_to_deliver).status = 'DELIVERED'

            Truck.update_distance(distance_to_add)

            Truck.update_location(myHash.search(packageID_to_deliver).address)

            for i in range(len(Truck.table)):
                distance_to_delivery_address = distance_data[look_up_dictionary[myHash.search(packageID_to_deliver).address]][look_up_dictionary[myHash.search(Truck.table[i]).address]]
                myHash.search(Truck.table[i]).distance = distance_to_delivery_address
            #print(packageID_to_deliver)
            Truck.table.remove(packageID_to_deliver)
    """





