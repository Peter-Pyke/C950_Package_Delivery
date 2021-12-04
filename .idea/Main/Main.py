from Package_Data import loadPackageData
from My_Hash_Table import getNumberOfItemsFromMyHash, ChainingHashTable
from Distance_Data import loadDistanceData, printDistanceMatrix

# Hash table instance
myHash = ChainingHashTable()

# Load packages to Hash Table
loadPackageData('CSV_Files/WGUPS Package File.csv', myHash)
printDistanceMatrix(loadDistanceData('CSV_Files/WGUPS Distance Table.csv'))

print("Packages from Hashtable:")
# Fetch data from Hash Table
#for i in range (int((getNumberOfItemsFromMyHash(myHash.table))/2)):
 #   print("Package: {}".format(myHash.search(i+1))) # 1 to 11 is sent to myHash.search()
