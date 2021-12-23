from Package_Data import loadPackageData, Package, getNumberOfItemsFromMyHash, display_package_data
from My_Hash_Table import ChainingHashTable
from Distance_Data import loadDistanceData, distanceLookUp
from Load_Trucks import load_truck
from Trucks import Truck
from datetime import datetime
from datetime import timedelta
from Nearest_Neighbor_Algorithm import deliver_packages
"""
Student Name:
Peter Chouinard

Student ID:
001162524
"""


# Hash table instance
myHash = ChainingHashTable()

# Loads dictionary with package addresses mapped to numeric values
look_up_dictionary = distanceLookUp('CSV_Files/hub_address_as_show_in_package_data.csv')

# Loads distance data into a list of lists
distance_data = loadDistanceData(('CSV_Files/WGUPS Distance Table.csv'))

# Loads packages to Hash Table
loadPackageData('CSV_Files/WGUPS Package File.csv', myHash, distance_data, look_up_dictionary)

# Truck one instance
truck_1 = Truck(0.0, datetime.strptime('2021-12-14 08:00 AM', "%Y-%m-%d %I:%M %p"), 1)
# Truck two instance
truck_2 = Truck(0.0, datetime.strptime('2021-12-14 09:05 AM', "%Y-%m-%d %I:%M %p"), 2)

# Initail loading of trucks
load_truck(myHash, truck_1)
load_truck(myHash, truck_2)
print("Packages on Truck_1:" + str(truck_1.table))
print("Packages on Truck_2:" + str(truck_2.table))
# Deliver packages and reload whichever truck returns first (in our case it will be truck_1)
while(len(truck_1.table)>0 or len(truck_2.table) > 0):
    deliver_packages(myHash, distance_data, look_up_dictionary, truck_1)
    deliver_packages(myHash, distance_data, look_up_dictionary, truck_2)
    if(truck_1.current_time < truck_2.current_time):
        load_truck(myHash, truck_1)
        print("Packages on Truck_1:" + str(truck_1.table))
    else:
        load_truck(myHash, truck_2)

# This loop checks for any packages being delivered late
for i in range(1, 41):
    if myHash.search(i).deadline < myHash.search(i).time_delivered:
        print("Package: " + str(myHash.search(i).ID) + " was late")

# Variable to hold user input
user_input_exit = "Y"

# This prompts the user for a time and will continue this loop until the users enters N
while(user_input_exit != "N"):
    user_input = input("Please enter a time in the following format: 10:30 AM")
    display_package_data(myHash, user_input, truck_1, truck_2)
    user_input_exit = input("\nWould you like to enter another time Y/N?")