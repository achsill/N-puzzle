import sys
from spiral_array import finalStateMatrix
from check_if_solvable import checkTheMatrix
from copy import copy, deepcopy
from math import sqrt;

def readFile():
    with open(sys.argv[1]) as f:
        content = f.readlines()
    return content;

def restructureList():
    fileContent = readFile();
    newList = [];
    for i, x in enumerate(fileContent):
        if i > 1:
            newList.append([int(n) for n in x.split()]);
    return newList;

def getPosition(matrix, value):
    for index, item in enumerate(matrix):
        newLen = len(item);
        for index2, item2 in enumerate(item):
            if item2 == value:
                return [index, index2];

def calculMisplacedTiles(matrix, finalMatrix, limit):
    i = 1;
    k = 0;
    k, result = (0,) *2;
    while (i < limit):
        j = getPosition(matrix, i);
        h = getPosition(finalMatrix, i);
        if j != h:
            k+=1;
        i+=1;
    return result;

# def calculNilssonSequence(matrix, finalMatrix, limit):

def calculManathanDistance(matrix, finalMatrix, limit):
    i = 1;
    result = 0;
    while (i < limit):
        j = getPosition(matrix, i);
        h = getPosition(finalMatrix, i);
        result = result + abs(j[0] - h[0]) + abs(j[1] - h[1]);
        i+=1;
    return result;

# Manathan + Linear distance.
def calculMandLdistance(matrix, finalMatrix, limit):
    result = 0;
    linearConf = 0;
    i = 1;
    while (i < limit):
        j = getPosition(matrix, i);
        h = getPosition(finalMatrix, i);
        if matrix[h[0]][h[1] - 1] == finalMatrix[h[0]][h[1]] and matrix[h[0]][h[1]] == finalMatrix[h[0]][h[1] - 1]:
            linearConf+=1;
        if matrix[h[0] - 1][h[1]] == finalMatrix[h[0]][h[1]] and matrix[h[0]][h[1]] == finalMatrix[h[0] - 1][h[1]]:
            linearConf+=1;
        if (abs(j[0] - h[0]) + abs(j[1] - h[1]) != 0):
            result = result + abs(j[0] - h[0]) + abs(j[1] - h[1]);
        i+=1;
    return result + linearConf * 2;


def getZeroPos(matrix):
    return getPosition(matrix, 0);

def calculAdjacent(matrix, finalMatrix, limit):
    zeroPos = getZeroPos(matrix);
    tmpMatrix = deepcopy(matrix);
    squareLimit = sqrt(limit);
    listNextNodes = [];
    if (zeroPos[1] + 1 < squareLimit):
        tmpMatrix[zeroPos[0]][zeroPos[1]], tmpMatrix[zeroPos[0]][zeroPos[1] + 1] = tmpMatrix[zeroPos[0]][zeroPos[1] + 1], tmpMatrix[zeroPos[0]][zeroPos[1]]
        listNextNodes.append(tmpMatrix);
        tmpMatrix = deepcopy(matrix);
    if (zeroPos[1] - 1 >= 0):
        tmpMatrix[zeroPos[0]][zeroPos[1] - 1], tmpMatrix[zeroPos[0]][zeroPos[1]] = tmpMatrix[zeroPos[0]][zeroPos[1]], tmpMatrix[zeroPos[0]][zeroPos[1] - 1]
        listNextNodes.append(tmpMatrix);
        tmpMatrix = deepcopy(matrix);
    if (zeroPos[0] + 1 < squareLimit):
        tmpMatrix[zeroPos[0]][zeroPos[1]], tmpMatrix[zeroPos[0] + 1][zeroPos[1]] = tmpMatrix[zeroPos[0] + 1][zeroPos[1]], tmpMatrix[zeroPos[0]][zeroPos[1]]
        listNextNodes.append(tmpMatrix);
        tmpMatrix = deepcopy(matrix);
    if (zeroPos[0] - 1 >= 0):
        tmpMatrix[zeroPos[0] -1][zeroPos[1]], tmpMatrix[zeroPos[0]][zeroPos[1]] = tmpMatrix[zeroPos[0]][zeroPos[1]], tmpMatrix[zeroPos[0] -1][zeroPos[1]];
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
            h = calculMandLdistance(matrix, finalMatrix, limit);
            if (i + h < m.f):
                m.h = h;
                m.g = i;
                m.parent = parent;
                return ;


def allPath(matrix):
    resultList = [];
    while matrix.parent is not None:
        resultList.append(matrix.matrix);
        matrix = matrix.parent;
    for i in reversed(resultList):
        for array in i:
            print array;
        print '\n';
    print "The program needed " + str(len(resultList)) + " moves to find the solution."
def aStar(matrix, finalMatrix, limit):
    closedList = [];
    openList = [];
    matrixInOpen = 1;
    openList.append(node(0, calculMandLdistance(matrix, finalMatrix, limit), matrix, None));
    while (openList is not None):
        currentMatrix = lowestFscore(openList);
        closedList.append(currentMatrix);
        openList.remove(currentMatrix);
        if (currentMatrix.matrix == finalMatrix):
            allPath(currentMatrix);
            print "Number of states been in the open list: " + str(matrixInOpen) + ".";
            return ;
        adjacentMatrix = calculAdjacent(currentMatrix.matrix, finalMatrix, limit);
        for aMatrix in adjacentMatrix:
            if matrixInList(closedList, aMatrix) == 1:
                continue;
            if matrixInList(openList, aMatrix) == 0:
                openList.append(node(currentMatrix.g + 1, calculMandLdistance(aMatrix, finalMatrix, limit), aMatrix, currentMatrix));
                matrixInOpen+=1;
            else:
                alreadyInOpenList(currentMatrix, openList, aMatrix, currentMatrix.g + 1, limit);



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
if checkTheMatrix(matrix, finalMatrix) == -1:
    print "this N-puzzle is not solvable";
    exit(0);
aStar(matrix, finalMatrix, nbrOfValue)
