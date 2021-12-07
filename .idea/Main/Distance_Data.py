import csv
matrix = []
for i in range(27):
    matrix.append([0] * 27)

def loadDistanceData(file_name):
    with open(file_name) as ourDistances:
        distance_data = csv.reader(ourDistances, delimiter=',')
        for hub in distance_data:
            for row in range(27):
                for column in range(27):
                    matrix[row][column] = hub[column]

    return matrix

def printDistanceMatrix(matrix, index_1, index_2):
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

