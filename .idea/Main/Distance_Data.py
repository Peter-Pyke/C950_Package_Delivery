import csv

matrix = []

def loadDistanceData(file_name):
    with open(file_name) as ourDistances:
        distance_data = csv.reader(ourDistances, delimiter=',')
        next(distance_data)
        for item in distance_data:
            matrix.append(item)

    return matrix

def printDistanceMatrix(matrix):
    for item in matrix:
        print(item)

def address_look_up(myHash):
    address_key_value = {}
    for i in range(0, 27):
        first_package_data = myHash.search(i)
        address_key_value[first_package_data.get_address()] = i
    return address_key_value



