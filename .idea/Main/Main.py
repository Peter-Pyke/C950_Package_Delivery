from Package_Data import loadPackageData, Package, getNumberOfItemsFromMyHash
from My_Hash_Table import ChainingHashTable
from Distance_Data import loadDistanceData, distanceLookUp
from Load_Trucks import load_truck_1, load_truck_2
from Trucks import Truck
from datetime import datetime
from Nearest_Neighbor_Algorithm import deliver_packages

# Hash table instance
myHash = ChainingHashTable()

# load dictionary with package addresses mapped to numeric value
look_up_dictionary = distanceLookUp('CSV_Files/hub_address_as_show_in_package_data.csv')

# Load distance data into a list of lists
distance_data = loadDistanceData(('CSV_Files/WGUPS Distance Table.csv'))

# Load packages to Hash Table
loadPackageData('CSV_Files/WGUPS Package File.csv', myHash, distance_data, look_up_dictionary)

# Print data from Hash Table
#print("Packages from Hashtable:")
#for i in range (int((getNumberOfItemsFromMyHash(myHash.table))/2)):
#    print("Package: {}".format(myHash.search(i+1))) # 1 to 40 is sent to myHash.search()

truck_1 = Truck(0.0, datetime.strptime('08:00 AM', "%I:%M %p"))
truck_2 = Truck(0.0, datetime.strptime('09:05 AM', "%I:%M %p"))

print(distance_data[look_up_dictionary['5383 South 900 East #104']][look_up_dictionary['3060 Lester St']])

load_truck_1(myHash, truck_1)
load_truck_2(myHash, truck_2)
print(truck_1.table)
print(truck_2.table)
#for i in range(16):
#    print(myHash.search(truck_1.table[i]).distance)
while(len(truck_1.table)>0):
    print(deliver_packages(myHash, distance_data, look_up_dictionary, truck_1))
#(truck_1.distance_traveled)
#print(truck_1.table)
#print(myHash.search(13).status)
