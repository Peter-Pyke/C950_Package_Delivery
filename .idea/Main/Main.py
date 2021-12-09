from Package_Data import loadPackageData, Package, getNumberOfItemsFromMyHash
from My_Hash_Table import ChainingHashTable
from Distance_Data import loadDistanceData, distanceLookUp
from Greedy_Algorithm import greedy_algorithm
from Trucks import Truck
from datetime import datetime


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

truck_1 = Truck(0, datetime.strptime('08:00 AM', "%I:%M %p"))
for i in range (1, 17):
    truck_1.insert(i)
print(truck_1.table)
print(truck_1.current_time)
print(myHash.search(15).truck)

my_package = myHash.search(5)
my_package_1 = myHash.search(1)
print("my_package", my_package.deadline )
print(my_package_1.deadline)
if my_package.deadline > my_package_1.deadline:
    print('It worked!')