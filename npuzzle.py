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
        # print "\negal = ", i, j, h, result
        i+=1;
    return result;

def getZeroPos(matrix):
    return getPosition(matrix, 0);

def calculH(matrix, finalMatrix, limit):
    zeroPos = getZeroPos(matrix);
    tmpMatrix = deepcopy(matrix);
    squareLimit = sqrt(limit);
    listNextNodes = [];
    if (zeroPos[1] + 1 < squareLimit):
        tmpMatrix[zeroPos[0]][zeroPos[1]], tmpMatrix[zeroPos[0]][zeroPos[1] + 1] = tmpMatrix[zeroPos[0]][zeroPos[1] + 1], tmpMatrix[zeroPos[0]][zeroPos[1]]
        # print "right = ", calculManathanDistance(tmpMatrix, finalMatrix, limit);
        listNextNodes.append(tmpMatrix);
        tmpMatrix = deepcopy(matrix);
    if (zeroPos[1] - 1 >= 0):
        tmpMatrix[zeroPos[0]][zeroPos[1] - 1], tmpMatrix[zeroPos[0]][zeroPos[1]] = tmpMatrix[zeroPos[0]][zeroPos[1]], tmpMatrix[zeroPos[0]][zeroPos[1] - 1]
        # print "left = ", calculManathanDistance(tmpMatrix, finalMatrix, limit);
        listNextNodes.append(tmpMatrix);
        tmpMatrix = deepcopy(matrix);
    if (zeroPos[0] + 1 < squareLimit):
        tmpMatrix[zeroPos[0]][zeroPos[1]], tmpMatrix[zeroPos[0] + 1][zeroPos[1]] = tmpMatrix[zeroPos[0] + 1][zeroPos[1]], tmpMatrix[zeroPos[0]][zeroPos[1]]
        # print "bot = ", calculManathanDistance(tmpMatrix, finalMatrix, limit);
        listNextNodes.append(tmpMatrix);
        tmpMatrix = deepcopy(matrix);
    if (zeroPos[0] - 1 >= 0):
        tmpMatrix[zeroPos[0] -1][zeroPos[1]], tmpMatrix[zeroPos[0]][zeroPos[1]] = tmpMatrix[zeroPos[0]][zeroPos[1]], tmpMatrix[zeroPos[0] -1][zeroPos[1]];
        # print "top = ", calculManathanDistance(tmpMatrix, finalMatrix, limit);
        listNextNodes.append(tmpMatrix);
        tmpMatrix = deepcopy(matrix);
    return listNextNodes;
def manathanDistance(matrix, finalMatrix, limit):
    openList = []
    # openList.append(node(0, calculManathanDistance(matrix, finalMatrix, limit, None), matrix));
    # i = 0;
    # print "skerg";
    # while (len(openList) > 0):
    #     if openList[i].matrix == finalMatrix:
    #         print "DONE";
    #
    #     listNodes = calculH(matrix, finalMatrix, limit,);
    #     print "skerg";
    #     i+=1;



class node:
    def __init__(self, g, h, matrix, parent):
        self.g = g;
        self.h = h;
        self.f = g + h;
        self.matrix = matrix;
        self.parent = parent;

matrix = restructureList();
nbrOfValue = len(matrix) * len(matrix);
finalMatrix = finalStateMatrix(matrix);
manathanDistance(matrix, finalMatrix, nbrOfValue)
