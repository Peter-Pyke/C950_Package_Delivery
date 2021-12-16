from Package_Data import loadPackageData, Package, getNumberOfItemsFromMyHash, display_package_data
from My_Hash_Table import ChainingHashTable
from Distance_Data import loadDistanceData, distanceLookUp
from Load_Trucks import load_truck
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
truck_1 = Truck(0.0, datetime.strptime('2021-12-14 08:00 AM', "%Y-%m-%d %I:%M %p"), 1)
# Truck two instance
truck_2 = Truck(0.0, datetime.strptime('2021-12-14 09:05 AM', "%Y-%m-%d %I:%M %p"), 2)

# Initail loading of trucks
load_truck(myHash, truck_1)
load_truck(myHash, truck_2)
print(truck_1.table)
print(truck_2.table)
# Deliver packages and reload whichever truck returns first
while(len(truck_1.table)>0 or len(truck_2.table) > 0):
    deliver_packages(myHash, distance_data, look_up_dictionary, truck_1)
    deliver_packages(myHash, distance_data, look_up_dictionary, truck_2)
    if(truck_1.current_time < truck_2.current_time):
        load_truck(myHash, truck_1)
    else:
        load_truck(myHash, truck_2)
    print(truck_1.table)
# Print data from Hash Table
#print("Packages from Hashtable:")
#for i in range (int((getNumberOfItemsFromMyHash(myHash.table))/2)):
#    print("Package: {}".format(myHash.search(i+1))) # 1 to 40 is sent to myHash.search()
for i in range(1, 41):
    if myHash.search(i).deadline < myHash.search(i).time_delivered:
        print('late', myHash.search(i))
print(truck_1.distance_traveled)
print(truck_2.distance_traveled)

user_input_exit = "Y"
while(user_input_exit != "N"):
    user_input = input("Please enter a time in the following format: 10:30 AM")
    display_package_data(myHash, user_input)
    user_input_exit = input("Would you like to enter another time Y/N?")