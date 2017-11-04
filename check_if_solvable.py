def finalList(finalMatrix):
    finalList = []
    for listM in finalMatrix:
        for nbr in listM:
            finalList.append(nbr);
    finalList.remove(0);
    return finalList;

def numberOfSwitches(matrix, limit):
    i = 1;
    k = 0;
    result = 0;
    while i < limit:
        k = 0;
        for p in matrix:
            for n in p:
                if i == n:
                    k = 1
                if n < i and k == 1 and n is not 0:
                    result+=1
        i+=1;
    return result;

def getZro(matrix):
    zeroPos = 0;
    for i, l in enumerate(reversed(matrix)):
        if 0 in l:
            return i + 1;
    return zeroPos

def checkTheMatrix(matrix, finalMatrix):
    squareMatrix = len(matrix);
    puissanceSquare = squareMatrix*squareMatrix;
    d = (numberOfSwitches(matrix, puissanceSquare) % 2);
    h = (numberOfSwitches(finalMatrix, puissanceSquare) % 2);
    if squareMatrix % 2 is not 0:
        if d == h:
            return 1;
        else:
            return -1;
    else:
        d = (getZro(matrix) + d) % 2;
        h = (getZro(finalMatrix) + h) % 2;
        if d == h:
            return 1;
        else:
            return -1;
