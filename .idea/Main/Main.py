from Package_Data import loadPackageData, Package, getNumberOfItemsFromMyHash
from My_Hash_Table import ChainingHashTable
from Distance_Data import loadDistanceData, distanceLookUp
from Load_Trucks import load_truck_1, load_truck_2, check_delivery_times_no_delay, check_delivery_times_delay_included, order_packages_by_deadline
from Trucks import Truck
from datetime import datetime
from datetime import timedelta
from Nearest_Neighbor_Algorithm import deliver_packages

# Hash table instance
myHash = ChainingHashTable()

# load dictionary with package addresses mapped to numeric value
look_up_dictionary = distanceLookUp('CSV_Files/hub_address_as_show_in_package_data.csv')

# Load distance data into a list of lists
distance_data = loadDistanceData(('CSV_Files/WGUPS Distance Table.csv'))

# Load packages to Hash Table
loadPackageData('CSV_Files/WGUPS Package File.csv', myHash, distance_data, look_up_dictionary)

# Truck one instance
truck_1 = Truck(0.0, datetime.strptime('08:00 AM', "%I:%M %p"))
# Truck two instance
truck_2 = Truck(0.0, datetime.strptime('09:05 AM', "%I:%M %p"))

# Initail loading of trucks
load_truck_1(myHash, truck_1)
load_truck_2(myHash, truck_2)

# Deliver packages and reload trucks as needed
while(len(truck_1.table)>0 or len(truck_2.table) > 0):
    deliver_packages(myHash, distance_data, look_up_dictionary, truck_1)
    deliver_packages(myHash, distance_data, look_up_dictionary, truck_2)
    if(truck_1.current_time < truck_2.current_time):
        load_truck_1(myHash, truck_1)
    else:
        load_truck_2(myHash, truck_2)

# Print data from Hash Table
print("Packages from Hashtable:")
for i in range (int((getNumberOfItemsFromMyHash(myHash.table))/2)):
    print("Package: {}".format(myHash.search(i+1))) # 1 to 40 is sent to myHash.search()
list = []
print(order_packages_by_deadline(myHash, list))
