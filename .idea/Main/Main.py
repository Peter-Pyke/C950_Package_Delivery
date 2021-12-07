from Package_Data import loadPackageData, Package
from My_Hash_Table import getNumberOfItemsFromMyHash, ChainingHashTable
from Distance_Data import loadDistanceData, printDistanceFromMatrix, distanceLookUp


# Hash table instance
myHash = ChainingHashTable()

# Load packages to Hash Table
loadPackageData('CSV_Files/WGUPS Package File.csv', myHash)
# Load distance data into a list of lists
myMatrix = loadDistanceData(('CSV_Files/WGUPS Distance Table.csv'))
# Load addresses of all hubs into a dicationary that maps them to a numeric value from 0 to 26
look_up_dictionary = distanceLookUp('CSV_Files/hub_address_as_show_in_package_data.csv')

""" The printDistanceFromMatrix function prints the distance between the two addresses passed to it.
    The second parater is using the look_up_dictionary function, to take the address from our Package
    object and turn it into a number that can be used as an index for our distance data in our matrix.
"""
printDistanceFromMatrix(myMatrix,  look_up_dictionary.get(myHash.search(2).address),0)


print("Packages from Hashtable:")
# Print data from Hash Table
for i in range (int((getNumberOfItemsFromMyHash(myHash.table))/2)):
    print("Package: {}".format(myHash.search(i+1))) # 1 to 40 is sent to myHash.search()
