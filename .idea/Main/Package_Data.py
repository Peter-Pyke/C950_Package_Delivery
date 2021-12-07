import csv

class Package:
    def __init__(self, ID, address, city, state, zip, deadline, mass, note):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.note = note

    def __str__(self):  # overwite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s,%s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip,
                                                  self.deadline, self.mass, self.note)
    def get_address(self):
        print(self.address)

def loadPackageData(fileName, my_hash):
    with open(fileName) as ourPackages:
        packageData = csv.reader(ourPackages, delimiter=',')
        next(packageData) # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pMass = package[6]
            pNote = package[7]
            pStatus = "Loaded"

            # package object
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pNote)


            # insert it into the hash table
            my_hash.insert(pID, p)


def getNumberOfItemsFromMyHash(hashtable):
    count = 0
    for item in hashtable:
        if type(item) == list:
            count += getNumberOfItemsFromMyHash(item)
        else:
            count += 1
    return count
