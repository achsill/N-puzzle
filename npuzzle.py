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

def alreadyInOpenList(parent, openList, matrix, i, limit, heuristic):
    for m in openList:
        if (m.matrix == matrix):
            h = chooseHeuristic(matrix, finalMatrix, limit, heuristic);
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

def allPath(matrix, web, matrixInOpen, sizeOpen):
    resultList = [];
    finalList = []
    while matrix.parent is not None:
        resultList.append(matrix.matrix);
        matrix = matrix.parent;
    resultList.append(matrix.matrix);
    if web == 0:
        for i in reversed(resultList):
            for array in i:
                print array;
            print '\n';
        print "The program needed " + str(len(resultList)) + " moves to find the solution."
        print "Number of states been in the open list: " + str(matrixInOpen) + ".";
        print "Maximum number of states ever represented in memory at the same time: " + str(sizeOpen) + ".";
    else:
        for i in reversed(resultList):
            nL = [];
            for array in i:
                nL.append(array);
            finalList.append(nL);
        data = {}
        data['steps'] = finalList;
        data['number_of_moves'] = len(resultList);
        data['number_in_openList'] = matrixInOpen;
        data['number_of_states'] = sizeOpen;
        json_data = json.dumps(data);
        print 'JSON: ', json_data;

def aStar(matrix, finalMatrix, limit, heuristic, web):
    closedList = [];
    openList = [];
    matrixInOpen = 1;
    openList.append(node(0, chooseHeuristic(matrix, finalMatrix, limit, heuristic), matrix, None));
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
            allPath(currentMatrix, web, matrixInOpen, sizeOpen);
            return ;
        adjacentMatrix = calculAdjacent(currentMatrix.matrix, finalMatrix, limit);
        for aMatrix in adjacentMatrix:
            if matrixInList(closedList, aMatrix) == 1:
                continue;
            if matrixInList(openList, aMatrix) == 0:
                priorityQueue(openList, (node(currentMatrix.g + 1, chooseHeuristic(aMatrix, finalMatrix, limit, heuristic), aMatrix, currentMatrix)));
                matrixInOpen+=1;
            else:
                alreadyInOpenList(currentMatrix, openList, aMatrix, currentMatrix.g + 1, limit, heuristic);


class node:
    def __init__(self, g, h, matrix, parent):
        self.g = g;
        self.h = h;
        self.f = g + h;
        self.matrix = matrix;
        self.parent = parent;

parse = restructureList();
matrix = parse[0];
nbrOfValue = len(matrix) * len(matrix);
finalMatrix = finalStateMatrix(matrix);
if checkTheMatrix(matrix, finalMatrix) == -1:
    print "this N-puzzle is not solvable";
    exit(0);
aStar(matrix, finalMatrix, nbrOfValue, parse[1], parse[2]);
