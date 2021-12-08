from Package_Data import loadPackageData, Package, getNumberOfItemsFromMyHash
from My_Hash_Table import ChainingHashTable
from Distance_Data import loadDistanceData, printDistanceFromMatrix, distanceLookUp
from Greedy_Algorithm import greedy_algorithm
from Trucks import Truck


# Hash table instance
myHash = ChainingHashTable()

# load dictionary with package addresses mapped to numeric value
look_up_dictionary = distanceLookUp('CSV_Files/hub_address_as_show_in_package_data.csv')

# Load distance data into a list of lists
distance_data = loadDistanceData(('CSV_Files/WGUPS Distance Table.csv'))

# Load packages to Hash Table
loadPackageData('CSV_Files/WGUPS Package File.csv', myHash, distance_data, look_up_dictionary)

truck_1 = Truck(0,'08:00')

loaded_truck = greedy_algorithm(myHash, truck_1)

print(truck_1)

# Print data from Hash Table
print("Packages from Hashtable:")
for i in range (int((getNumberOfItemsFromMyHash(myHash.table))/2)):
    print("Package: {}".format(myHash.search(i+1))) # 1 to 40 is sent to myHash.search()
