import csv
matrix = []

def loadDistanceData(file_name):
    with open(file_name) as ourDistances:
        distance_data = csv.reader(ourDistances, delimiter=',')
        next(distance_data) # skip header
        for hub in distance_data:
                matrix.append(hub)
    return matrix

def printDistanceFromMatrix(matrix, index_1, index_2):
    print(matrix[index_1][index_2])


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

