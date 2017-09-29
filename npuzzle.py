import sys
from spiral_array import finalStateMatrix
from copy import copy, deepcopy
from math import sqrt;

def readFile():
    with open(sys.argv[1]) as f:
        content = f.readlines()
    return content;

def restructureList():
    fileContent = readFile();
    newList = [];
    for x in fileContent:
         newList.append([int(n) for n in x.split()]);
    return newList;

def getPosition(matrix, value):
    for index, item in enumerate(matrix):
        newLen = len(item);
        for index2, item2 in enumerate(item):
            if item2 == value:
                return [index, index2];



def calculManathanDistance(matrix, finalMatrix, limit):
    i = 1;
    k, result = (0,) *2;
    while (i < limit):
        j = getPosition(matrix, i);
        h = getPosition(finalMatrix, i);
        result = result + abs(j[0] - h[0]) + abs(j[1] - h[1]);
        i+=1;
    return result;

def getZeroPos(matrix):
    return getPosition(matrix, 0);

# def moveRight(matrix):

def manathanDistance(matrix, finalMatrix, limit):
    zeroPos = getZeroPos(matrix);
    tmpMatrix = deepcopy(matrix);
    squareLimit = sqrt(limit);
    if (zeroPos[1] + 1 < squareLimit):
        matrix[zeroPos[0]][zeroPos[1]], matrix[zeroPos[0]][zeroPos[1] + 1] = matrix[zeroPos[0]][zeroPos[1] + 1], matrix[zeroPos[0]][zeroPos[1]]
        matrix = deepcopy(tmpMatrix);
        print "right = ", calculManathanDistance(matrix, finalMatrix, limit);
    if (zeroPos[1] - 1 >= 0):
        matrix[zeroPos[0]][zeroPos[1] - 1], matrix[zeroPos[0]][zeroPos[1]] = matrix[zeroPos[0]][zeroPos[1]], matrix[zeroPos[0]][zeroPos[1] - 1]
        print "left = ", calculManathanDistance(matrix, finalMatrix, limit);
    if (zeroPos[0] + 1 < squareLimit):
        matrix[zeroPos[0]][zeroPos[1]], matrix[zeroPos[0] + 1][zeroPos[1]] = matrix[zeroPos[0] + 1][zeroPos[1]], matrix[zeroPos[0]][zeroPos[1]]
        print "top = ", calculManathanDistance(matrix, finalMatrix, limit);
    if (zeroPos[0] - 1 >= 0):
        matrix[zeroPos[0] -1][zeroPos[1]], matrix[zeroPos[0]][zeroPos[1]] = matrix[zeroPos[0]][zeroPos[1]], matrix[zeroPos[0] -1][zeroPos[1]];
        print "bot = ", calculManathanDistance(matrix, finalMatrix, limit);
# def changePos(grid):
#     for index, item in enumerate(grid):
#         for index2, item2 in enumerate(item):
#             if (item2 == 0):
#                 item[index2], item[index2 + 1] = item[index2 + 1], item[index2]
#                 return grid;
#     return grid;

class node:
    def __init__(self, g, h):
        self.g = g;
        self.h = h;
        self.f = g + h;
    def get_f():
        return self.f;

matrix = restructureList();
nbrOfValue = len(matrix) * len(matrix);
finalMatrix = finalStateMatrix(matrix);
print matrix;
print finalMatrix;
manathanDistance(matrix, finalMatrix, nbrOfValue)
print matrix;
