import csv

# This returns a list of lists containing all the distances between all the address as show in the distance table file
def loadDistanceData(file_name):
    matrix = []
    with open(file_name) as ourDistances:
        distance_data = csv.reader(ourDistances, delimiter=',')
        next(distance_data) # skip header
        for hub in distance_data:
                matrix.append(hub)
    return matrix

# This maps all the addresses to a numeric value, which will be used as an index when retrieving the distance data
# from the matrix above
def distanceLookUp(file_name):
    with open(file_name) as addresses:
        address_data = csv.reader(addresses, delimiter=',')
        look_up_dic = {}
        next(address_data) # skip header
        count = 0
        for address in address_data:
            look_up_dic[address[0]] = count
            count += 1
        return look_up_dic

