from copy import copy, deepcopy

def chooseHeuristic(matrix, finalMatrix, limit, i):
    if i == 1:
        return calculMandLdistance(matrix, finalMatrix, limit);
    elif i == 2:
        return calculManathanDistance(matrix, finalMatrix, limit);
    elif i == 3:
        return calculMisplacedTiles(matrix, finalMatrix, limit);

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

def calculManathanDistance(matrix, finalMatrix, limit):
    i = 1;
    result = 0;
    while (i < limit):
        j = getPosition(matrix, i);
        h = getPosition(finalMatrix, i);
        result = result + abs(j[0] - h[0]) + abs(j[1] - h[1]);
        i+=1;
    return result;

def horizontalConf(matrix, finalMatrix, j, h, i, linear, workedList):
    actualLine = deepcopy(matrix[j[0]]);
    goalLine = deepcopy(finalMatrix[j[0]]);
    workingList = [];
    for x in actualLine:
        if x in goalLine and x != 0:
            workingList.append(x);
    if i in workingList:
        workingList.remove(i);
        if j != h:
            for x in workingList:
                if x in goalLine:
                    tmpPos = getPosition(matrix, x);
                    if h[1] <= tmpPos[1] <= j[1]:
                        linear+=1;
                    elif j[1] <= tmpPos[1] <= h[1]:
                        linear+=1
    return linear;

def verticalConf(matrix, finalMatrix, j, h, i, linear, workedList):
    actualLine = [];
    goalLine = [];
    d = 0;
    while d < len(matrix):
        actualLine.append(matrix[d][j[1]]);
        goalLine.append(finalMatrix[d][j[1]]);
        d+=1;
    d = 0;
    workingList = [];
    for x in actualLine:
        if x in goalLine and x != 0:
            workingList.append(x);
    if i in workingList:
        workingList.remove(i);
        if j != h:
            for x in workingList:
                if x in goalLine:
                    tmpPos = getPosition(matrix, x);
                    if h[0] <= tmpPos[0] <= j[0]:
                        linear+=1;
                    elif j[0] <= tmpPos[0] <= h[0]:
                        linear+=1
    return linear;


def isLinearConflit(matrix, finalMatrix, limit):
    i = 1;
    workedList = [];
    linear = 0;
    while (i < limit):
        j = getPosition(matrix, i);
        h = getPosition(finalMatrix, i);
        linear = horizontalConf(matrix, finalMatrix, j, h, i, linear, workedList);
        linear = verticalConf(matrix, finalMatrix, j, h, i, linear, workedList);
        i+=1;
    return linear;

# Manathan + Linear distance.
def calculMandLdistance(matrix, finalMatrix, limit):
    result = 0;
    linearConf = 0;
    i = 1;
    while (i < limit):
        j = getPosition(matrix, i);
        h = getPosition(finalMatrix, i);
        if (abs(j[0] - h[0]) + abs(j[1] - h[1]) != 0):
            result = result + abs(j[0] - h[0]) + abs(j[1] - h[1]);
        i+=1;
    return result + isLinearConflit(matrix, finalMatrix, limit);

def getPosition(matrix, value):
    for index, item in enumerate(matrix):
        newLen = len(item);
        for index2, item2 in enumerate(item):
            if item2 == value:
                return [index, index2];
