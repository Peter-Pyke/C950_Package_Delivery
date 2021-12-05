from Package_Data import loadPackageData, Package
from My_Hash_Table import getNumberOfItemsFromMyHash, ChainingHashTable
from Distance_Data import loadDistanceData, printDistanceMatrix

# Hash table instance
myHash = ChainingHashTable()

# Matrix holding all the distance data
myMatrix = loadDistanceData('.idea/CSV_Files/WGUPS Distance Table.csv')

# Print Matrix data
printDistanceMatrix(myMatrix)

# Load packages to Hash Table
loadPackageData('.idea/CSV_Files/WGUPS Package File.csv', myHash)

# Print header
print("Packages from Hashtable:")

# Print data from Hash Table
for i in range (int((getNumberOfItemsFromMyHash(myHash.table))/2)):
    print("Package: {}".format(myHash.search(i+1))) # 1 to 40 is sent to myHash.search()
for i in range(1, 27):
    first_package_data = myHash.search(i)
    first_package_data.get_address()