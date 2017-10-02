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

def lowestFscore(matrixList):
    lowest = None;
    for matrix in matrixList:
        if (lowest is None):
            lowest = matrix;
        if (matrix.f < lowest.f):
            lowest = matrix;
    return lowest;

def matrixInList(matrixList, matrix):
    for m in matrixList:
        if (m.matrix == matrix):
            return 1;
    return 0;

def alreadyInOpenList(parent, openList, matrix, i, limit):
    for m in openList:
        if (m.matrix == matrix):
            h = calculManathanDistance(matrix, finalMatrix, limit);
            if (i + h < m.f):
                m.h = h;
                m.g = i;
                m.parent = parent;
                return ;


def allPath(matrix):
    while matrix.parent is not None:
        print matrix.matrix;
        matrix = matrix.parent;

def manathanDistance(matrix, finalMatrix, limit):
    closedList = [];
    openList = [];
    openList.append(node(0, calculManathanDistance(matrix, finalMatrix, limit), matrix, None));
    while (openList is not None):
        currentMatrix = lowestFscore(openList);
        closedList.append(currentMatrix);
        openList.remove(currentMatrix);
        if (currentMatrix.matrix == finalMatrix):
            allPath(currentMatrix);
            return ;
        adjacentMatrix = calculH(currentMatrix.matrix, finalMatrix, limit);
        for aMatrix in adjacentMatrix:
            if matrixInList(closedList, aMatrix) == 1:
                continue;
            if matrixInList(openList, aMatrix) == 0:
                openList.append(node(currentMatrix.g + 1, calculManathanDistance(aMatrix, finalMatrix, limit), aMatrix, currentMatrix));
            else:
                alreadyInOpenList(currentMatrix, openList, aMatrix, currentMatrix.g + 1, limit);
    print "this N-puzzle is not solvable";
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
