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


