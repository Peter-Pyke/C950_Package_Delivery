import csv
matrix = []
for i in range(27):
    matrix.append([0] * 27)

def loadDistanceData(file_name):
    with open(file_name) as ourDistances:
        distance_data = csv.reader(ourDistances, delimiter=',')
        next(distance_data) # skip header
        for hub in distance_data:
            for row in range(27):
                for column in range(27):
                    matrix[row][column] = hub[column]
    return matrix

def printDistanceMatrix(matrix):
    for row, col in range(len(matrix)):
        print(matrix[row][col])

