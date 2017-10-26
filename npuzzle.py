from spiral_array import finalStateMatrix
from check_if_solvable import checkTheMatrix
from copy import copy, deepcopy
from math import sqrt
from heuristics import *
from readFile import restructureList
import math
import json

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

def priorityQueue(currList, toAdd):
    for i, x in enumerate(currList):
        if x.f > toAdd.f:
            currList.insert(i, toAdd);
            return ;
    currList.append(toAdd);

def allPath(matrix):
    resultList = [];
    finalList = []
    while matrix.parent is not None:
        resultList.append(matrix.matrix);
        matrix = matrix.parent;
    resultList.append(matrix.matrix);
    for i in reversed(resultList):
        nL = [];
        for array in i:
            nL.append(array);
            print array;
        finalList.append(nL);
        print '\n';
    print "The program needed " + str(len(resultList)) + " moves to find the solution."
    # for website
    # data = {}
    # data['steps'] = finalList;
    # data['number_of_moves'] = 3;
    # data['number_in_openList'] = 8;
    # json_data = json.dumps(data);
    # print 'JSON: ', json_data;

def aStar(matrix, finalMatrix, limit):
    closedList = [];
    openList = [];
    matrixInOpen = 1;
    openList.append(node(0, calculMandLdistance(matrix, finalMatrix, limit), matrix, None));
    sizeOpen = None;
    while (openList is not None):
        if sizeOpen is None:
            sizeOpen = len(openList);
        else:
            if len(openList) > sizeOpen:
                sizeOpen = len(openList);
        currentMatrix = openList[0];
        closedList.append(currentMatrix);
        openList.remove(currentMatrix);
        if (currentMatrix.matrix == finalMatrix):
            allPath(currentMatrix);
            print "Number of states been in the open list: " + str(matrixInOpen) + ".";
            print "Maximum number of states ever represented in memory at the same time: " + str(sizeOpen) + ".";
            return ;
        adjacentMatrix = calculAdjacent(currentMatrix.matrix, finalMatrix, limit);
        for aMatrix in adjacentMatrix:
            if matrixInList(closedList, aMatrix) == 1:
                continue;
            if matrixInList(openList, aMatrix) == 0:
                priorityQueue(openList, (node(currentMatrix.g + 1, calculMandLdistance(aMatrix, finalMatrix, limit), aMatrix, currentMatrix)));
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
