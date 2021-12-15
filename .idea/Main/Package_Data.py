import csv
from Distance_Data import distanceLookUp
from datetime import datetime



class Package:
    def __init__(self, ID, address, city, state, zip, deadline, mass, note, status, distance):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.note = note
        self.status = status
        self.distance = distance
        self.no_delay = True
        self.truck = None
        self.time_delivered = None
        self.time_loaded_on_truck = None

    def __str__(self):  # overwite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip,
                                        self.deadline, self.mass, self.note, self.status, self.distance, self.time_delivered, self.time_loaded_on_truck)
    def update_distance(self, distance):
        self.distance = distance


def loadPackageData(fileName, my_hash, distance_data, look_up_dictionary):
    with open(fileName) as ourPackages:
        packageData = csv.reader(ourPackages, delimiter=',')
        next(packageData) # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = datetime.strptime(package[5], "%m/%d/%y %I:%M %p")
            pMass = package[6]
            pNote = package[7]
            pStatus = "AT HUB"
            pDistance = distance_data[0][look_up_dictionary.get(pAddress)]
            # package object
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pNote, pStatus, pDistance)
            if (pID == 6) or (pID == 9) or (pID == 25) or (pID == 28) or (pID == 32):
                p.no_delay = False
            if (pID == 3) or (pID == 18) or (pID == 36) or (pID == 38):
                p.truck = 2
            if (pID ==13) or (pID == 14) or (pID == 15) or (pID == 16) or (pID == 19) or (pID == 20):
                p.truck = 1
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

