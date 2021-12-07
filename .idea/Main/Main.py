from Package_Data import loadPackageData, Package
from My_Hash_Table import getNumberOfItemsFromMyHash, ChainingHashTable
from Distance_Data import loadDistanceData, printDistanceMatrix, distanceLookUp

# Hash table instance
myHash = ChainingHashTable()

# Load packages to Hash Table
loadPackageData('CSV_Files/WGUPS Package File.csv', myHash)
myMatrix = loadDistanceData(('CSV_Files/WGUPS Distance Table.csv'))
look_up_dictionary = distanceLookUp('CSV_Files/hub_address_as_show_in_package_data.csv')
print(look_up_dictionary.get('2530 S 500 E'))
print(look_up_dictionary)
print(myHash.search(2))
print(myHash.search(2).address)
print(myMatrix[9][0])
printDistanceMatrix(myMatrix,  look_up_dictionary.get(myHash.search(2).address),0)


print("Packages from Hashtable:")
# Fetch data from Hash Table
#for i in range (int((getNumberOfItemsFromMyHash(myHash.table))/2)):
 #   print("Package: {}".format(myHash.search(i+1))) # 1 to 11 is sent to myHash.search()
